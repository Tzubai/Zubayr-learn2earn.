import json

# Load saved passwords
try:
    with open("passwords.json", "r") as file:
        passwords = json.load(file)
except FileNotFoundError:
    passwords = {}


while True:
    print("==============================")
    print("       CLI BROWSER")
    print("==============================")
    website = input("\nEnter website (or 'exit'): ")

    if website == "exit":
        break

    # Check if website is already saved
    if website in passwords:
        print("\nSaved password found!")

        username = passwords[website]["username"]
        password = passwords[website]["password"]

        print("Username:", username)
        print("Password:", password)

        login = input("Login automatically? (Y/N): ").upper()

        if login == "Y":
            print("Logged in successfully!")

    else:
        print("\nNo saved password.")

        username = input("Enter username: ")
        password = input("Enter password: ")

        save = input("Save this password? (Y/N): ").upper()

        if save == "Y":
            passwords[website] = {
                "username": username,
                "password": password
            }

            with open("passwords.json", "w") as file:
                json.dump(passwords, file, indent=4)

            print("Password saved!")
