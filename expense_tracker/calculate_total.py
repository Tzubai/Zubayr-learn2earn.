from packages import *

def calculate_total(expenses):

    if not expenses:
        print("No expenses available to calculate.")
        return

    total = sum(expense["amount"] for expense in expenses)

    print(f"=====Total spending=====\n"
          f"₦{(total):>5,.2f}"
          )
    input("Press enter to return options.")
    subprocess.run(["clear"])
    time.sleep(1)

