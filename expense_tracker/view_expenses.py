from packages import *

def view_expenses(expenses):

    if not expenses:
        print("No expenses recorded yet.")
        return

    print(print_header_line())
    print(print_header())
    print(print_header_line())

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i:<20}"
            f"₦{expense['amount']:<20,.2f}"
            f"{expense['category']:<20}"
            f"{expense['description']:<20}"
        )

    print(print_header_line())

    input("Press enter to continue.")
    subprocess.run(["clear"])
    time.sleep(1)

