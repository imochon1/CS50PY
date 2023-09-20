# try is what is meant to be accomplished / except is what to do if it fails and else is what to do if it succeeds
def main():
    x = get_int("Whats is x : ")  # prompt
    print(f"x is {x}")


def get_int(prompt):  # prompt is the message that will be displayed
    while True:
        try:
            return int(input(prompt))
        except ValueError:  # ValueError
            pass  # pass will just continue the loop until it succeeds
        # else:
        # wHAT TO DO IF IT SUCCEEDS


main()
