name = input('Enter your name: ')
# Remove whitespace from str
name = name.strip()

# Capitalize
name = name.title()

#split
first , second = name.split()

#Remove whitespace from str and Capitalize at once
# name = name.strip()name.title()

print("hello", second)
#print Format :
#print(f"hello, {name}")


