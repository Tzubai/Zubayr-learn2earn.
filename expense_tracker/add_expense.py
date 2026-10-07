import subprocess
import string
import time

def ispunctuation(word):
    punctuations = string.punctuation
    if word not in punctuations:
        return False
    return True


block = False
def add_expense(expenses, save_expenses, view_expenses, le, something):
    while True:
        category = input(
            "What category of expense do you want to add (or type 'back' to cancel): "
        ).strip().lower()

        if category == "back":
            time.sleep(1)
            return

        if category == "":
            print("Category cannot be empty.")
            continue


        if all(char.isdigit() or ispunctuation(char) for char in category):
            print("Category must contain a letter.")
            continue

        if len(category) > 10:
            print("Category is too long. Maximum is 10 characters.")
            continue

        break

    while True:
        description = input(
            "Specify description: "
        ).strip()

        if description == "":
            print("Description can't be empty.")
            continue

        if all(char.isdigit() or ispunctuation(char) for char in description):
            print("Description must contain a o8letter.")
            continue

        if len(description) > 30:
            print("Description is too long. Maximum is 30 characters.")
            continue

        break

    while True:
        try:
            amount = round(float(input("Specify amount: ₦")), 2)

            if amount < 1:
                print("Please enter a valid amount.")
                continue

            if amount > 1_000_000:
                print("Amount cannot be more than ₦1,000,000.")
                continue

            break

        except ValueError:
            print("Only numbers allowed.")

    expenses.append({
        "amount": amount,
        "category": category,
        "description": description
    })

    save_expenses()

    while True:
        view = input(
            "Expense added successfully. "
            "Do you want to view your expenses? Y/N: "
        ).strip().lower()

        if view == "":
            print("Space can't be empty.")
            continue

        elif view == "y":
            print("All expenses:")
            view_expenses(expenses, le, something)
            return

        elif view == "n":
            block = True
            break

        else:
            print("Invalid input.")

    if block == True:
        subprocess.run(["clear"])
        return
    else:
        input("Press enter to continue.")
        subprocess.run(["clear"])
        time.sleep(1)
