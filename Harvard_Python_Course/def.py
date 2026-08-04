def main():
    greeting()
    name = input("Enter your name: ")
    greeting(name)

def greeting(to = "world"):
    print("Hello!", to)

main()
