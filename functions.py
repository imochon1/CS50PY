# Define a function def and always follow with a colon : ex: def hello():


# Ask for name
def main():
    name = input("What is your name? ")
    hello(name)


def hello(to="world"):
    print("Hello,", to)


main()
