def main():
    hello("Alice")
    goodbye("Bob")


def hello(name):
    print("Hello " + name)


def goodbye(name):
    print("Goodbye " + name)


if __name__ == "__main__":
    main()

# The __name__ variable is set to "__main__" when the script is run directly. If the script is imported, __name__ is #set to the name of the script. This allows you to have code that is run when the script is run directly, but not when #it is imported.
