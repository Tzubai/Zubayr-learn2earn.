package main

import (
	"bytes"
	"fmt"
	"net/http"
	"os"
	"strings"
	"text/template"
)

func main() {
	http.HandleFunc("/", homePage)
	// http.HandleFunc("/ascii-art", asciiArt)
	fmt.Println("server running at: http://localhost:8080")
	http.ListenAndServe(":8080", nil)
}

func homePage(w http.ResponseWriter, r *http.Request) {
	if r.URL.Path != "/" {
		http.Error(w, "Page does not exist", http.StatusNotFound) //http.StatusNotFound int value = 404
		return
	}
	t, err := template.ParseFiles("page.html")
	if err != nil {
		http.Error(w, "Template not found", http.StatusInternalServerError) //http.StatusInternalServerError int value == 500
		return
	}

	var out string
	if r.Method == "POST" {
		banner := r.FormValue("banner")
		str := r.FormValue("text")
		if str == "" {
			http.Error(w, "Enter text", http.StatusBadRequest) //http.StatusBadRequest int value == 400
			return
		}

		out, err = asciiArt(str, banner)
		if err != nil {
			http.Error(w, "Banner file does not exist", http.StatusNotFound)
			return
		}
	}
	var container bytes.Buffer

	err = t.Execute(&container, out)
	if err != nil {
		http.Error(w, "Failure to execute template", http.StatusInternalServerError)
		return
	}
	w.Write(container.Bytes())
}

func asciiArt(str string, banner string) (string, error) {
	var msg strings.Builder
	fonts, err := os.ReadFile(banner + ".txt")
	if err != nil {
		return "", err
	}
	// for windows \n is seen as \r\n(\r > carriage return and \n > newline)
	font := strings.ReplaceAll(string(fonts), "\r\n", "\n")
	fontStrings := font
	splitted_font := strings.Split(fontStrings, "\n")

	splitted_str := strings.Split(str, "\r\n")

	for i, word := range splitted_str {
		if i == 0 && word == "" {
			continue
		}
		if word == "" {
			msg.WriteString("\n")
			continue
		}
		for i := 0; i < 8; i++ {
			for _, ch := range word {
				start_index := int(9*(ch-32) + 1)
				msg.WriteString(splitted_font[start_index+i])
			}
			msg.WriteString("\n")
		}
	}
	return msg.String(), nil
}
// func main() {
// 	// Multiplexer : where all path are saved
// 	m := http.NewServeMux()
// 	m.HandleFunc("/", home)
// 	fmt.Println("server is running...")
// 	http.ListenAndServe(":8080", m)

// 	// this is the default and it is less secured.
// 	// http.HandleFunc("/", home)
// 	// http.ListenAndServe(":8080", nil)
// }

// func home(w http.ResponseWriter, r *http.Request) {
// 	t, _ := template.ParseFiles("page.html")
// 	value := r.FormValue("banner")
// 	t.Execute(w, value)
// 	// fmt.Fprintln(w, "hello world")
// if err != nil {
// 	http.Error(w, "Template not found", http.StatusNotFound)
// 	return
// }
// fmt.Println(r.Header)
// r.header
// for k, v := range r.Header {
// 	fmt.Println(k, v)
// }
// ma := map[string]string{"banner":value, "text": str }
// }

// 	// text := r.FormValue("text")
// 	// banner := r.FormValue("banner")

// 	// generate ascii art here
// }

// func main() {

// 	ma := map[string]int{}
// 	ma["ade"] = 10
// 	ma["bola"] = 15
// 	ma["shade"] = 10
// 	ma["law"] = 20

// 	for k, v := range ma {
// 		if v == 10 {
// 			fmt.Println(k)
// 		}
// 	}
// }
