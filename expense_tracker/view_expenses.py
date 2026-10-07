import subprocess
import time

def view_expenses(expenses, le, some):

    if not expenses:
        print("No expenses recorded yet.")
        return

    print("=" * le)

    print(some)

    print("=" * le)


    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i:<20}"
            f"₦{expense['amount']:<20,.2f}"
            f"{expense['category']:<20}"
            f"{expense['description']:<20}"
        )

    print("=" * le)

    input("Press enter to continue.")
    subprocess.run(["clear"])
    time.sleep(1)

