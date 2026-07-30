package main

import (
	"fmt"
	"html/template"
	"net/http"
	"strconv"
	"strings"
)

type Account struct {
	Name    string
	Balance float64
}

type PageData struct {
	Accounts  []Account
	Message   string
	Success   bool
	HasResult bool
}

var accounts = []Account{
	{"Zubayr", 1000},
	{"Usman", 500},
	{"Aisha", 1500},
	{"Maryam", 800},
}

var tmpl = template.Must(template.ParseFiles("index.html"))

func findAccount(name string) (*Account, bool) {
	name = strings.TrimSpace(name)

	for i := range accounts {
		if strings.EqualFold(accounts[i].Name, name) {
			return &accounts[i], true
		}
	}
	return nil, false
}

func main() {
	http.HandleFunc("/", transfer)

	fmt.Println("Server running on http://localhost:8080")
	http.ListenAndServe(":8080", nil)
}

func transfer(w http.ResponseWriter, r *http.Request) {

	data := PageData{
		Accounts: accounts,
	}

	if r.Method == http.MethodPost {

		data.HasResult = true

		senderName := strings.TrimSpace(r.FormValue("sender"))
		receiverName := strings.TrimSpace(r.FormValue("receiver"))
		amountStr := strings.TrimSpace(r.FormValue("amount"))

		if senderName == "" || receiverName == "" {
			data.Message = "❌ Sender and receiver are required."
			tmpl.Execute(w, data)
			return
		}

		if strings.EqualFold(senderName, receiverName) {
			data.Message = "❌ Sender and receiver cannot be the same."
			tmpl.Execute(w, data)
			return
		}

		sender, found := findAccount(senderName)
		if !found {
			data.Message = "❌ Sender account does not exist."
			tmpl.Execute(w, data)
			return
		}

		receiver, found := findAccount(receiverName)
		if !found {
			data.Message = "❌ Receiver account does not exist."
			tmpl.Execute(w, data)
			return
		}

		amount, err := strconv.ParseFloat(amountStr, 64)

		if err != nil {
			data.Message = "❌ Amount must be a valid number."
			tmpl.Execute(w, data)
			return
		}

		if amount <= 0 {
			data.Message = "❌ Amount must be greater than zero."
			tmpl.Execute(w, data)
			return
		}

		if amount > sender.Balance {
			data.Message = fmt.Sprintf(
				"❌ Insufficient funds. %s only has $%.2f",
				sender.Name,
				sender.Balance,
			)
			tmpl.Execute(w, data)
			return
		}

		// Transfer
		sender.Balance -= amount
		receiver.Balance += amount

		data.Success = true
		data.Message = fmt.Sprintf(
			"✅ $%.2f transferred from %s to %s successfully.",
			amount,
			sender.Name,
			receiver.Name,
		)

		data.Accounts = accounts
	}

	tmpl.Execute(w, data)
}