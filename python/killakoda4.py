import time
import random
import sys
# random_number = random.randint(1, 100)
# print(random_number)
# import random
# random_number = random.randint(1, 20)

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


# print("Welcome to the number counter.\n")
# num = input("Enter digits of your choice: ")

# while not num.isdigit():
#     print("Ops!! Numbers only!")
#     num = input("Enter digits only: ")

# count = 0

# for digit in num:
#     count += 1

# print(count)




# word = input("Enter a word: ")

# reverse = ""

# for character in word:
#     reverse = reverse

# print("Reverse:", reverse)

# if word == reverse:
#     print("This is a palindrome!")
# else:
#     print("This is not a palindrome.")




name = input("What is your name?: ")
if name == "":
    name = "Player"

print("Welcome", name)

while True:
    try:
        starting_number = int(input("Enter the starting number: "))
        ending_number = int(input("Enter the ending number: "))

        if (ending_number < starting_number) or (ending_number == starting_number):
            print("The starting number cannot be greater than the ending number.")
            print("Please try again.")
            continue
        break
    except ValueError:
        print("Only whole numbers are allowed. Please try again.")

random_number = random.randint(starting_number, ending_number)
print(random_number)

tries = 0
remaining = 0
trial_times = 0

while True:
    try:
        trial_times = int(input("How many guesses would you like?: "))
        if trial_times <= 0:
            print("You must allow at least 1 guess.")
            continue

        break
    except ValueError:
        print("Only whole numbers are allowed. Please try again.")

for i in range(trial_times):
    while True:
        try:
            guess = int(input(
                f"Guess the number ({starting_number}-{ending_number}): "
                ))

            if guess < starting_number or guess > ending_number:
                print(
                    f"Please enter a number between "
                    f"{starting_number} and {ending_number}."
                )
                continue
            break

        except ValueError:
                   print("Only whole numbers are allowed. Try again.")

    tries += 1

    remaining = trial_times - tries
    if guess == random_number:
        print("Correct!")

        if tries == 1:
            print(f"You guessed correctly in {tries} try!!!. {remaining} tries remaining")
        else:
            print(f"You guessed correctly in {tries} tries. {remaining} tries remaining")
        break
    elif guess > random_number:
        print("Number too high!")
    else:
        print("Number too low!")

    remaining = trial_times - tries

    if remaining == 1:
        print("You have 1 try remaining.")
    elif remaining > 1:
        print(f"You have {remaining} tries remaining.")

if guess != random_number:
    print("Ops!!, You didn't guess the number. The number was:", random_number)

