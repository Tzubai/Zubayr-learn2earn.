from packages import *

def delete_expense(expenses):

    if not expenses:
        print("No expenses available yet.")
        return

    print("Available expenses.")
    print_header_line()
    print_header()
    print_header_line()

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i:<20}"
            f"₦{expense['amount']:<20,.2f}"
            f"{expense['category']:<20}"
            f"{expense['description']:<20}"
        )
    print_header_line()

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

            answer = input("Do you want to continue with your delete? Y/N: .")
            if answer == "y":
                del expenses[delete - 1]
                save_expenses(expenses)
                break
            elif answer == "n":
                block = True
                continue
            else:
                print("Invalid input.")
                break

        except ValueError:
            print("Please enter a number.")

    print("Expense deleted successfully.")
    print("Available expenses.")
    view_expenses(expenses)
    subprocess.run(["clear"])
    time.sleep(1)

