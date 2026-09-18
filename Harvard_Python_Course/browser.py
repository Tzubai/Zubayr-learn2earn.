import json

def load_passwords():
    try:
        with open("passwords.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return {}

def save_passwords(passwords):
    with open("passwords.json", "w") as file:
        json.dump(passwords, file, indent=4)

def visit_website(passwords):

    website = input("\nEnter website: ")

    if website in passwords:

        print("\nSaved password found!")

        username = passwords[website]["username"]
        password = passwords[website]["password"]

        print("Username:", username)
        print("Password:", password)

        login = input("Login automatically? (yes/no): ")

        if login == "yes":
            print("Logged in successfully!")

    else:

        print("\nNo saved password.")

        username = input("Enter username: ")
        password = input("Enter password: ")

        save = input("Save this password? (yes/no): ")

        if save == "yes":

            passwords[website] = {
                "username": username,
                "password": password
            }

            save_passwords(passwords)

            print("Password saved!")

def main():

    passwords = load_passwords()

    while True:

        print("==============================")
        print("       CLI BROWSER")
        print("==============================")
        print("1. Visit website")
        print("2. Exit")

        choice = input("Choose: ")

        if choice == "1":
            visit_website(passwords)

        elif choice == "2":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")
main()
