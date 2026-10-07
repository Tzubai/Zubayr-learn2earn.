import json
import time
import sys

from add_expense import add_expense, ispunctuation
from view_expenses import view_expenses
from calculate_total import calculate_total
from calculate_cate import calculate_by_category
from delete_expense import delete_expense
from exit_program import exit_program



def main():
    try:
        def save_expenses():
            with open("expenses.json", "w") as file:
                json.dump(expenses, file, indent=4)


        def load_expenses():
            try:
                with open("expenses.json", "r") as file:
                    data = json.load(file)

                    if not isinstance(data, list):
                        print("Invalid JSON structure. Expenses must be a list.")
                        return []
                    return data

            except FileNotFoundError:
                print("No json file")
                return []

            except json.JSONDecodeError:
                print("The JSON file is corrupted.")
                return []

        expenses = load_expenses()

        pr = (
                f"{'Index':<20}"
                f"{'Amount':<20}"
                f"{'Category':<20}"
                f"{'Description':<20}"
            )
        le = len(pr)

        while True:

            time.sleep(0.1)
            print("\n======== Expense Tracker ========")

            choice = input(
                "1- Add an expense\n"
                "2- View all expenses\n"
                "3- Calculate total spending\n"
                "4- Calculate spending by category\n"
                "5- Delete an expense\n"
                "6- Exit\n"
                "Choose an option: "
            )

            try:
                choice = int(choice)

                if choice < 1 or choice > 6:
                    print("That number does not exist in the options.")
                    continue

            except ValueError:
                print("Please enter a number.")
                continue

            if choice == 1:
                add_expense(expenses, save_expenses, view_expenses, le, pr)

            elif choice == 2:
                view_expenses(expenses, le, pr)

            elif choice == 3:
                calculate_total(expenses)

            elif choice == 4:
                calculate_by_category(expenses)

            elif choice == 5:
                delete_expense(expenses, pr, le, save_expenses, view_expenses)

            elif choice == 6:
                exit_program()

    except (KeyboardInterrupt, EOFError):
        sys.exit()

# if __name__ == "__main__":
main()
