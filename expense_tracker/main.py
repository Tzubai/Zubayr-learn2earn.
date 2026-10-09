from packages import *

def main():
    try:
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
                if choice == 6:
                    exit_program()
                else:
                    subprocess.run(["clear"])
                    time.sleep(0.5)

            except ValueError:
                print("Please enter a number.")
                continue
            match choice:
                case 1:
                    add_expense(expenses)
                case 2:
                    view_expenses(expenses, )
                case 3:
                    calculate_total(expenses)
                case 4:
                    calculate_by_category(expenses)
                case 5:
                    delete_expense(expenses)
                case 6:
                    exit_program()

    except (KeyboardInterrupt, EOFError):
        return

if __name__ == "__main__":
    main()
