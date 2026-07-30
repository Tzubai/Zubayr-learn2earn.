package main

import (
	"strings"
)

func capitalize(i int, str []string) []string {
	if str[i] == "cap" {
		str[i-1] = strings.ToUpper(string(str[0])) + str[i-1][1:]
	}
	return (str)
}

func UpperCase(i int, str []string) []string {
	if str[i] == "up" {
		str[i-1] = strings.ToUpper(str[i-1])
	}
	return str
}

func LowerCase(i int, str []string) []string{
	if str[i] == "low" {
		str[i-1] = strings.ToLower(str[i-1])
	}
	return str
}
