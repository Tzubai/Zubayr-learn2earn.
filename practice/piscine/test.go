package main

import "fmt"

// func main() {
// 	(LastRune("Hello!"))
// 	(LastRune("Salut!"))
// 	(LastRune("Ola!"))
// 	fmt.Println('\n')
// }

// func LastRune(s string) rune {
// 	ch := len(s)-1
// 	fmt.Println(rune(ch[]))
// }
//   func printComb() {
// 	for i:= 0; i <= 7; i++ {
// 		for j:= i + 1; j <= 8; j++ {
// 			for k:= j + 1; k <= 9; k++ {
// 				fmt.Print(i)
// 				fmt.Print(j)
// 				fmt.Print(k)
// 				if i != 7{
// 					fmt.Print(", ")
// 				}
// 			}
// 		}
// 	}
// 	fmt.Println()
//   }

//   func main() {
// 	printComb()
//   }
func printComb() {
	for i := 0; i <= 7; i++ {
		for j := 1; j <= 8; j++ {
			for k := 2; k <= 9; k++ {
				if i != j && i != k && j != k && j > i && k > j {
					fmt.Print(i)
					fmt.Print(j)
					fmt.Print(k)
					if i != 7 {
						fmt.Print(", ")
					}
				}
			}
		}
	}
	fmt.Println()
}

func main() {
	printComb()
}

