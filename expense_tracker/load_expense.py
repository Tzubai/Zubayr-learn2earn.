from packages import *

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
