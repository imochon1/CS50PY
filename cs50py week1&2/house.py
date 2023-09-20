name = input("What is your name? ")

match name:
    case "Harry" | "Ron" | "Hermione":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case "Luna":
        print("Ravenclaw")
    case _:
        print("WHO?")
