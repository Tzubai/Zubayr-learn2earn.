import subprocess
import time

def delete_expense(expenses, pr, le, save_expenses, view_expenses):

    if not expenses:
        print("No expenses available yet.")
        return

    print("Available expenses.")
    print("=" * le)

    print(pr)

    print("=" * le)


    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i:<20}"
            f"₦{expense['amount']:<20,.2f}"
            f"{expense['category']:<20}"
            f"{expense['description']:<20}"
        )

    print("=" * le)


    while True:

        delete = input(
            "Choose an expense to delete from the list above (or type 'back' to cancel): "
        ).strip().lower()

        if delete == "back":
            time.sleep(1)
            return


        try:
            delete = int(delete)

            if delete < 1 or delete > len(expenses):
                print("That expense number does not exist.")
                continue

            del expenses[delete - 1]

            save_expenses()

            break

        except ValueError:
            print("Please enter a number.")

    print("Expense deleted successfully.")
    print("Available expenses.")
    view_expenses(expenses, le, pr)

    input("Press enter to continue.")
    subprocess.run(["clear"])
    time.sleep(1)

