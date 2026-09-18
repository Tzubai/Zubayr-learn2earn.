package main

import (
	"fmt"
	"html/template"
	"net/http"
	"os"
	"strings"
)

var tmpl *template.Template
var err error

func main() {
	http.HandleFunc("/", Get)
	http.HandleFunc("/ascii-art", Post)
	fmt.Println("Server running at:http://localhost:8080")
	http.ListenAndServe(":8080", nil)
}
func Get(w http.ResponseWriter, r *http.Request) {
	if r.URL.Path != "/" {
		http.Error(w, "Page not found", http.StatusNotFound)
		return
	}
	if r.Method != http.MethodGet {
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
		return
	}
	tmpl, err = template.ParseFiles("template/index.html")
	if err != nil {
		http.Error(w, "Internal server error", http.StatusInternalServerError)
		return
	}
	tmpl.Execute(w, nil)
}
func Post(w http.ResponseWriter, r *http.Request) {
	if r.URL.Path != "/ascii-art" {
		http.Error(w, "Page not found", http.StatusNotFound)
		return
	}
	if r.Method != http.MethodPost {
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
		return
	}
	text := r.FormValue("text")
	if text == "" {
		http.Error(w, "Bad request", http.StatusBadRequest)
		return
	}
	banner := r.FormValue("banner")
	final, err := ascii(text, banner)
	if err != nil {
		http.Error(w, "Corrupted banner file", http.StatusNotFound)
		return
	}
	tmpl.Execute(w, final)
}
func ascii(text string, banner string) (string, error) {
	font, err := os.ReadFile(banner + ".txt")
	if err != nil {
		return "", err
	}
	replaced := strings.ReplaceAll(string(font), "\r\n", "\n")
	splitted := strings.Split(replaced, "\n")

	str := strings.Split(text, "\r\n")

	var msg strings.Builder
	for j, ch := range str {
		if j == 0 && ch == "" {
			continue
		}
		if ch == "" {
			msg.WriteString("\n")
			continue
		}
		for i := 0; i < 8; i++ {
			for _, word := range ch {
				formula := int(word-32)*9 + 1 + i
				msg.WriteString(splitted[formula])
			}
			msg.WriteString("\n")
		}
	}
	return msg.String(), nil
}
