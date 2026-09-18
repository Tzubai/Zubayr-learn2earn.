import sys
# num = int(input("Enter A Number: "))

# if num < 10 :
#     print(num,"Is Too High!")
# else:
#     print(num,"Is A Valid Number")



# password = input("Enter Your Password: ").upper()

# if password == "PASSWORD" :
#     print("Login Successful")
# else:
#     print("Invalid Password")



# name = input("Enter Your Name: ").title()

# if name == "Tom" :
#     print("Hello", name)
# else:
#     print("Sorry We Are Expecting Tom")



# print("Enter 3 Numbers")
# num1 = int(input("First Number: "))
# num2 = int(input("Second Number: "))
# num3 = int(input("Third Number: "))


# if num1 == num2 or num1 == num3 or num2 == num3:
#     print("Snap!!! You have entered same numbers")
#     sys.exit()

# if num2 > num1 and num3 > num1:
#     print("Your first number  is the smallest")
# elif num1 > num2 and num3 > num2:
#     print("Your second number  is the smallest")
# else:
#     print("Your third number  is the smallest")


# # if num1 > num2:
# #     print("Your first number is higher than the second number")
# # else:
# #     print("Your second number is higher than the first number")


# print("How much have you gathered")

# a = int(input("First: $"))
# b = int(input("Second: $"))
# c = int(input("Third: $"))

# total = a+b+c

# if total >= 1000:
#     grant = total * 2
#     print(f"Total gathered is: ${total}\nYou have been granted double of what you gathered: ${grant}")


print("Enter 3 words")
a = input("1st word: ").lower()
b = input("2nd word: ").lower()
c = input("3rd word: ").lower()

if a == b and b == c:
    print("all three are the same")
elif a == b or b == c or a == c:
    print("two words are the same")
else:
    print("there are no words that are the same")
