def main():

    x = float(input("What the height? "))
    y = float(input("What is the width? "))
    # print("The perimeter of your triangle is: ", perimeter(x, y))
    # s = pe
    print(f"The perimeter of your triangle is: {perimeter(x,y):.2f}")

def perimeter(x, y):
    # perimeter = (x ** 2) + (y ** 2)
    # perimeter = round(perimeter, 2)
#rounding of numbers
    return pow(x, 2) + pow(y, 2)

#it can also be done from the print format
# print(f"Your answer is {z:.2f}")
main()
