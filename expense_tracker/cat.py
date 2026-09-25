# expenses = []
expenses = [
    {"amount": 600, "category": "food", "description": "rice\n"},
    {"amount": 1500, "category": "transport", "description": "car"},
    {"amount": 400, "category": "food", "description": "amala\n"},
    # {"amount": 1000, "category": "food", "description": "bread"}
]

name = input("What is your name?: ")
print("Welcome", name)
print("Select an option ")
choice = input("1- add an expense\n2- View all expenses\n3- Calculate total spending\n4- Calculate spending by category\n5- Delete an expense\n5- Exit\n")


if choice == "1":
    category = input("What category of expense do you want to add: ")
    description = input("Specify description: ")
    amount = float(input("Specify amount: "))
    expenses.append({"amount": amount, "category": category, "description": description})
if choice == "2":
    print(expenses)
if choice == "3":
    # total = 0
    # for i in range(len(expenses)):
    #     total += expenses[i]["amount"]
    total = sum(expense["amount"] for expense in expenses)
    print(total)
if choice == "4":
    categories = []

    for expense in expenses:
        if expense["category"] not in categories:
            categories.append(expense["category"])
    print(f"Available categories:\n{categories}")

    calculate_category = input("What category of expense do you want to calculate?: ")
    total = 0

    for expense in expenses:
        if expense["category"] == calculate_category:
            total += expense["amount"]

    print(f"Total spending on {calculate_category} is {total}")
