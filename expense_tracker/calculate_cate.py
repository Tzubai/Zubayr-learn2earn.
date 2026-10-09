from packages import *

def calculate_by_category(expenses):

    if not expenses:
        print("No expenses available to calculate.")
        return

    categories = []

    for expense in expenses:
        if expense["category"] not in categories:
            categories.append(expense["category"])

    print(f"Available categories:\n{categories}")

    while True:

        calculate_category = input(
            "What category of expense do you want to calculate? (or type 'back' to cancel): "
        ).strip().lower()

        if calculate_category == "back":
            time.sleep(1)
            return

        if calculate_category not in categories:
            print("Category not available.")
            continue

        total = 0

        for expense in expenses:
            if expense["category"] == calculate_category:
                total += expense["amount"]

        break

    print(
        f"Total spending on {calculate_category}: "
        f"₦{total:,.2f}"
    )
    input("Press enter to return options.")
    subprocess.run(["clear"])
    time.sleep(1)

