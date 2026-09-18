import sys
# names = ["Ellie", "Dan", "Perry", "Justin"]
# food = ["Apple", 3, "Chocolate", 3, "Sandwich", 4, "Cake", 1]
# print(names)
# print(food)

# name1 = "Ellie"
# name2 = "Dan"
# student_id = [name1, name2]
# print(student_id)




# myList = ["fish",
#           "beans",
#           "amala",
#           "eba"]
# print(f"My favourite foods are: {", ".join(myList)}")




# fruits = ["mango", "orange", "banana", "pawpaw", "water-melon"]

# num = int(input("Choose one number (0, 1, 2, 3, 4) : "))

# print(fruits[num])



# fruits = ["mango", "orange", "banana", "pawpaw", "water-melon"]
# fruits.append("pineapple")
# fruits.insert(1,"apple")
# fruits.remove("pawpaw")
# print(fruits)
# print(fruits)
# removed = fruits.pop()
# print(fruits)
# print(removed)


# numbers = [10, 90, 23, 46, -20]
# removed_number = numbers.pop()
# print(numbers)
# print(len(numbers))
# print(removed_number)

# numbers = [10, 90, 23, 46, -20]
# removed_number = numbers.pop(-2)
# print(numbers)
# print(len(numbers))
# print(removed_number)


# fruits = ["mango", "orange", "banana", "pawpaw", "water-melon"]
# print(fruits[-1])



# items = ["mango", "orange", "banana", "pawpaw", "water-melon"]
# print("Add 3 more items for free")
# items.append(input("1st: "))
# items.append(input("2nd: "))
# items.append(input("3rd: "))

# print(f"All items: {", ".join(items)}")
# print(f"Total item: {len(items)}")



# countries = ["china", "Nigeria", "Ghana", "Mali", "USA"]
# print(countries)
# remove = input("Do you want to remove one of the non-african country? Y/N: ").upper()

# if remove == "Y":
#     select = input("First or Last: ").upper()
#     if select == "FIRST":
#         # print(f"This is the new countries list: {countries[1:]}")
#         countries.remove("china")
#         print(countries)
#     elif select == "LAST":
#         print(f"This is the new countries list: {countries[:-1]}")
#     else:
#         print("Invalid Input")
# elif remove == "N":
#     print(f"No country removed: {countries}")
#     sys.exit()
# else:
#     print("Invalid Input")




library = ["fiqh", "hadith", "aqeedah", "manhaj", "tajweed", "tawheed"]
# library = []
print(library)
answer = input("Do you want to add to or remove from this book arrangement? ADD/REMOVE: ").upper()

if answer == "ADD":
    book = input("Add the book: ")
    if book == "":
        print("No book was added")
        sys.exit()
    if book in library:
        print("Book already existed!!")
        sys.exit()
    position = int(input("Where should it be positioned?: "))
    if library == [] and position >=1:
        library.append(book)
        print(library)
        sys.exit()
    if position > 0 and position <= len(library):
        position = position - 1
        library.insert(position,book)
        print(library)
    else:
        print("Position out of range pls recheck!!!")
        sys.exit()
elif answer == "REMOVE":
    remove = input("Which book do you want to remove?: ")
    if remove in library:
        library.remove(remove)
        print(library)
    else:
        print("Book not in library, Recheck!!!")
        sys.exit()
else:
    print("Invalid Input")
    sys.exit()

