# loops

# while loop
# i = 3
# while i != 0:
#    print("Meow")
#    i -= 1  # IF we dont subtract i, it will be an infinite loop because i will always be 3

# b = 0
# while b < 3:
#    print("Meow")
#    b += 1


# for loops
# for _ in range(
#    3
# ):  # [] is a list and range is a function that returns a list of numbers from 0 to a set number
#    print(
#        "Meow for loop", _
#    )  # _ is a variable that is used to store the value of the current iteration


# print(
#    "Meow\n" * 3, end=""
# )
# # end="" is used to remove the new line at the end of the print statement
# \n is a new line character

# while True:
#    n = int(input("Enter a number: "))
#    if n > 0:
#        break

# for _ in range(n):
#    print("Meow")


def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("Enter a number: "))
        if n > 0:
            return n


def meow(n):
    for _ in range(n):
        print("Meow")


main()
