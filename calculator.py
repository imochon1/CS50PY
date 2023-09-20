# Addition ,Float and Integers
# x = float(input("Enter a number: "))

# y = float(input("Enter another number: "))

# The input function returns a string, so we need to convert it to an integer with int()
# print(int(input("Enter a number: ")) + int(input("Enter another number: ")))
# z = int(x) + int(y)
# Round the number
# z = round(x + y)

# z = round(x / y, 2) # Round to 2 decimal places print(f"{z:.2f}")

# z = x / y


# print(f"{z:,}") # This is a formatted string literal that adds commas to the number z for readability


# print(f"{z:.2f}")


def main():
    x = int(input("Enter a number: "))
    print(f"The square of {x} is {square(x)}")


def square(n):  # retuurn pow(n, 2) # or also n ** 2
    return n * n


main()
