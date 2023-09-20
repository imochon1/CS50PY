import sys  # import sys module

if len(sys.argv) < 2:
    print("Too few arguments")
    sys.exit()

for arg in sys.argv[1:]:
    print("Hello, my name is", arg)  # Ver comment de slices


# [:] slices the list,takes the colon to indicate that we want to slice the list, and then takes the empty string to indicate that we want to slice the entire list. This is equivalent to writing [0:4] or [0:len(cards)].

# sys.exit() is a function that terminates the program. It can be used to exit the program if the user enters too many or too few arguments. It can also be used to exit the program if the user enters invalid arguments.
# sys.argv Has to be concatenated with a string because it can only be passed one argument at a time

# sys.argv is a list that contains all the command line arguments passed to a Python script. The first element of the list is the name of the Python script itself. The second element of the list is the first argument passed to the script. The third element of the list is the second argument passed to the script, and so on.
