package main

import "fmt"

type Profile struct {
	FullName string
	Age int
	height float64
	IsRegister bool
	IsTaller bool
}

func main() {
	user1 := Profile{
		"teelad",
		26,
		45.8,
		true,
		false,
	}

	user2 := Profile{
		Age: 27,
		FullName: "ade",
		height: 40.6,
		IsRegister: true,
	}

	fmt.Println(user1)
	fmt.Println(user2)

	if user1.height > user2.height {
		user1.IsTaller = true
	}else{
		user2.IsTaller = true
	}

	fmt.Println("User1: ",user1.IsTaller)
	fmt.Println("User2: ",user2.IsTaller)

	user3 := Profile{}

	user3.FullName ="labake"

	fmt.Println(user3)

}