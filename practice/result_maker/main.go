package main

import (
	"fmt"
	"net/http"
	"strconv"
	"text/template"
)

// Subject holds one subject's name and score
type Subject struct {
	Name  string
	Score float64
	Grade string
	Remark string
}

// PageData is everything the HTML page will display
type PageData struct {
	StudentName string
	Subjects    []Subject
	Average     float64
	FinalGrade  string
	FinalRemark string
	HasResult   bool
}

var tmpl = template.Must(template.ParseFiles("index.html"))

func main() {
	http.HandleFunc("/", grade)
	fmt.Println("Server running at http://localhost:8080")
	http.ListenAndServe(":8080", nil)
}

// getGrade converts a score into a letter grade and remark
func getGrade(score float64) (string, string) {
	switch {
	case score >= 90:
		return "A", "Excellent 🌟"
	case score >= 80:
		return "B", "Very Good 👍"
	case score >= 70:
		return "C", "Good ✅"
	case score >= 60:
		return "D", "Pass ⚠️"
	default:
		return "F", "Fail ❌"
	}
}

func grade(w http.ResponseWriter, r *http.Request) {
	data := PageData{}

	if r.Method == "POST" {
		data.HasResult = true
		data.StudentName = r.FormValue("name")

		// List of subjects we're grading
		subjectNames := []string{"Mathematics", "English", "Science", "History"}
		formFields := []string{"math", "english", "science", "history"}

		var total float64
		var count float64

		for i, field := range formFields {
			scoreStr := r.FormValue(field)
			score, err := strconv.ParseFloat(scoreStr, 64)

			var subject Subject
			subject.Name = subjectNames[i]

			if err != nil || score < 0 || score > 100 {
				subject.Score = 0
				subject.Grade = "?"
				subject.Remark = "Invalid score"
			} else {
				subject.Score = score
				subject.Grade, subject.Remark = getGrade(score)
				total += score
				count++
			}

			data.Subjects = append(data.Subjects, subject)
		}

		if count > 0 {
			data.Average = total / count
			data.FinalGrade, data.FinalRemark = getGrade(data.Average)
		}
	}

	tmpl.Execute(w, data)
}