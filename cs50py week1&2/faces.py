def main():
    mood = input("Enter your Mood: ")
    mood = convert(mood)
    print(mood)


def convert(mood):
    mood = mood.replace(":)", "🙂")
    mood = mood.replace(":(", "🙁")
    return mood


main()
