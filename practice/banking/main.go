package main

import (
	"html/template"
	"net/http"
	"strconv"
	"strings"
	"sync"
)

type Account struct {
	Name    string
	Balance float64
}

type Transaction struct {
	Sender   string
	Receiver string
	Amount   float64
}

type PageData struct {
	Accounts     []Account
	Transactions []Transaction
	Message      string
	IsError      bool
}

var mu sync.Mutex

var accounts = []Account{
	{"Zubayr", 1000},
	{"Usman", 500},
	{"Aisha", 1500},
	{"Maryam", 800},
}

var transactions []Transaction

func findAccount(name string) *Account {
	name = strings.TrimSpace(name)
	for i := range accounts {
		if strings.EqualFold(accounts[i].Name, name) {
			return &accounts[i]
		}
	}
	return nil
}

func render(w http.ResponseWriter, msg string, err bool) {
	t := template.Must(template.ParseFiles("templates/index.html"))

	data := PageData{
		Accounts:     accounts,
		Transactions: transactions,
		Message:      msg,
		IsError:      err,
	}

	t.Execute(w, data)
}

func home(w http.ResponseWriter, r *http.Request) {
	if r.Method == http.MethodGet {
		render(w, "", false)
		return
	}

	mu.Lock()
	defer mu.Unlock()

	sender := findAccount(r.FormValue("sender"))
	receiver := findAccount(r.FormValue("receiver"))

	if sender == nil || receiver == nil {
		render(w, "Account not found", true)
		return
	}

	if sender == receiver {
		render(w, "Cannot transfer to same account", true)
		return
	}

	amount, err := strconv.ParseFloat(r.FormValue("amount"), 64)
	if err != nil || amount <= 0 {
		render(w, "Invalid amount", true)
		return
	}

	if amount > sender.Balance {
		render(w, "Insufficient balance", true)
		return
	}

	sender.Balance -= amount
	receiver.Balance += amount

	transactions = append([]Transaction{
		{sender.Name, receiver.Name, amount},
	}, transactions...)

	render(w, "Transfer successful", false)
}

func main() {
	http.HandleFunc("/", home)
	println("http://localhost:8080")
	http.ListenAndServe(":8080", nil)
}