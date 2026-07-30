package main

import "fmt"

// // quest 2
// // printalphabet
// func main() {
// 	for i := 'a'; i <= 'z'; i ++ {
// 		fmt.Print(string(i))
// 	}
// 	fmt.Println()
// }

// // // printreversealphabet
// func main() {
// 	for i := 'z'; i >= 'a'; i-- {
// 		fmt.Print(string(i))
// 	}
// 	fmt.Println()
// }

// // printdigits
// func main() {
// 	for i := 0; i <= 9; i++ {
// 		fmt.Print(i)
// 	}
// 	fmt.Println()
// }

// // isnegative
// func main() {
// 	IsNegative(1)
// 	IsNegative(0)
// 	IsNegative(-1)
// }

// func IsNegative(nb int) {
// 	if nb < 0 {
// 		fmt.Println("T")
// 	}else{
// 		fmt.Println("F")
// 	}
// }

// // PrintComb
// func PrintComb() {
// 	for i := 0; i <= 7; i++ {
// 		for j := 1; j <= 8; j++ {
// 			for k := 2; k <= 9; k++ {
// 				if i != j && i != k && j != k && j > i && k > j {
// 					fmt.Print(i)
// 					fmt.Print(j)
// 					fmt.Print(k)
// 					if i != 7 {
// 						fmt.Print(", ")
// 					}
// 				}
// 			}
// 		}
// 	}
// 	fmt.Println()
// }

// func main() {
// 	PrintComb()
// }

// func PrintComb() {
// 	for i := 0; i <= 7; i++ {
// 		for j := i + 1; j <= 8; j++ {
// 			for k := j + 1; k <= 9; k++ {
// 				fmt.Print(i)
// 				fmt.Print(j)
// 				fmt.Print(k)
// 				if i != 7 {
// 					fmt.Print(", ")
// 				}
// 			}
// 		}
// 	}
// 	fmt.Println()
// }

// // PrintComb2
// func main() {
// 	PrintComb2()
// }

// func PrintComb2() {
// 	for i := 0; i <= 9; i++ {
// 		for j := 0; j <= 9; j++ {
// 			for k := i; k <= 9; k++ {
// 				for l := k; l <= 9; l++ {
// 					if i != k || j != l {
// 						fmt.Print(i)
// 						fmt.Print(j)
// 						fmt.Print(" ")
// 						fmt.Print(k)
// 						fmt.Print(l)
// 						// if i != 9 || j != 8 || k != 9 || l != 9 {
// 						if !(i == 9 && j == 8 && k == 9 && l == 9) {
// 							fmt.Print(", ")
// 						}
// 					}
// 				}
// 			}

// 		}
// 	}
// 	fmt.Println()
// }

func PrintNbr(n int) {
	if n < 0 {
		fmt.Print("-")
		n = -n
	}
	var str string
	for n > 0 {
		d := n % 10
		c := rune(d) + '0'
		str = string(c) + str
		n = n / 10
	}
	fmt.Print(str)
}

func main() {``
	PrintNbr(-123)
	PrintNbr(0)
	PrintNbr(123)
	fmt.Println()
}