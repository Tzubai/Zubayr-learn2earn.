package main

import (
	"fmt"
	"os"
	"slices"
	"strings"
)

func main() {
	if len(os.Args) != 3 {
		fmt.Println("Usage: go run . input.txt output.txt")
		return
	}
	input := os.Args[1]
	output := os.Args[2]

	sample, err := os.ReadFile(input)
	if err != nil {
		fmt.Println("Error reading input file")
	}
	str := strings.Fields(string(sample))
	for i := 0; i < len(str); i++ {
			capitalize(i, str)
			UpperCase(i, str)
			LowerCase(i, str)
			str = slices.Delete(str, i, i+1)
			i--
	}
	content := strings.Join(str, " ")
	os.WriteFile(output, []byte(content), 0666)
}
