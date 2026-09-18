import time
import random
random_number = random.randint(1, 100)

# i = 1
# while i < 3:
#     print(i)
#     i += 1
# print("loop has finished")


# i = 1
# while i <= 3:
#     print(i)
#     i += 1


# i = 1
# while i == 3:
#     print(i)
#     i += 1


# i = 1
# while True:
#     print(i)
#     time.sleep(0.1)
#     i += 1


# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         break
#     print(i)




# name = input("Your name pls: ")
# print("Welcome", name)
# password = ""
# user_pass = input("\nEnter your password: ").upper()
# trial = 1

# while user_pass != "PASSWORD":
#     user_pass = input("Incorrect password, try again: ").upper()
#     trial += 1

# print("Correct password")
# if trial == 1:
#     print("You Unlocked you device with 1 trial")
# else:
#     print(f"You Unlocked your device with {trial} trials")



# count = 0
# total = 0
# highest = 0
# lowest = 10

# while True:

#     try:
#         score = int(input("Enter a score between 1 and 10(0 to stop!!!): "))
#     except ValueError:
#         print("Invalid Input! Enter a number between 1 - 10. ")
#         continue

#     if score == 0:
#         break
#     if score < 1 or score > 10:
#         print("Invalid Input! Enter a number between 1 - 10. ")
#         continue

#     count += 1
#     total += score

#     if score > highest:
#             highest = score
#     if score < lowest:
#         lowest = score


#     average = total / count

# print("\n===== RESULTS =====")
# print("Total score:", total)
# print("Number of scores:", count)
# print("Highest score:", highest)
# print("Average score:", average)
# print("Lowest score:", lowest)





# guess = 0
# tries = 0

# while guess != random_number:

#     while True:
#         try:
#             guess = int(input("Guess the number: "))
#             break
#         except ValueError:
#             print("Only numbers are allowed. Try again.")

#     if guess > random_number:
#         print("Number too high!")

#     if guess < random_number:
#         print("Number too low!")

#     tries += 1

# print("Correct!")
# if tries == 1:
#     print(f"You needed only {tries} try to guess the number!!!")
# else:
#     print(f"You needed {tries} tries to guess the number!!!")











# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
# print("I have finished the loop")



# for x in "banana":
#     print(x)


# fruits = ["apple", "banana", "cherry"]
# for j in range(len(fruits)):
#     print(fruits[j])
#     if fruits[j] == "banana":
#         break


print("Welcome to the number counter.\n")
num = input("Enter digits of your choice: ")

while not num.isdigit():
    print("Ops!! Numbers only!")
    num = input("Enter digits only: ")

count = 0

for digit in num:
    count += 1

print(count)



# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)
