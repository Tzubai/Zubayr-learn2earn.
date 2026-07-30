package main

import (
	"fmt"
	"math"
	"net/http"
	"strconv"
	"text/template"
)

// This struct holds all the data we send to our HTML page
type Result struct {
	HasResult bool
	Message   string
	Root1     string
	Root2     string
}

// Load our HTML file once at startup
var tmpl = template.Must(template.ParseFiles("index.html"))

func main() {
	// When someone visits "/", run the "solve" function
	http.HandleFunc("/", solve)

	fmt.Println("Server running at http://localhost:8080")
	http.ListenAndServe(":8080", nil)
}

func solve(w http.ResponseWriter, r *http.Request) {
	result := Result{}

	// Only do math when the user submits the form (POST request)
	if r.Method == "POST" {
		// Read the three values the user typed in
		a, errA := strconv.ParseFloat(r.FormValue("a"), 64)
		b, errB := strconv.ParseFloat(r.FormValue("b"), 64)
		c, errC := strconv.ParseFloat(r.FormValue("c"), 64)

		// Check if all inputs are valid numbers
		if errA != nil || errB != nil || errC != nil {
			result.Message = "❌ Please enter valid numbers for a, b, and c."
		} else if a == 0 {
			result.Message = "❌ 'a' cannot be zero — that's not a quadratic equation!"
		} else {
			// The magic formula: D = b² - 4ac
			discriminant := b*b - 4*a*c
			result.HasResult = true

			if discriminant > 0 {
				// Two different real roots
				x1 := (-b + math.Sqrt(discriminant)) / (2 * a)
				x2 := (-b - math.Sqrt(discriminant)) / (2 * a)
				result.Message = "✅ Two real roots found:"
				result.Root1 = fmt.Sprintf("x₁ = %.4f", x1)
				result.Root2 = fmt.Sprintf("x₂ = %.4f", x2)

			} else if discriminant == 0 {
				// Exactly one root
				x := -b / (2 * a)
				result.Message = "✅ One real root (repeated):"
				result.Root1 = fmt.Sprintf("x = %.4f", x)

			} else {
				// No real roots (imaginary numbers)
				result.Message = "ℹ️ No real roots — discriminant is negative."
			}
		}
	}

	// Send the result to the HTML page
	tmpl.Execute(w, result)
}