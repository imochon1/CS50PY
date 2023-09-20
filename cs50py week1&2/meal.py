def main():
    answer = input("What time is it? ")
    time = convert(answer)
    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")


def convert(time):
    # if time donesn't end with a.m. or p.m. then it's in 24 hour format:
    if not time.endswith("a.m.") and not time.endswith("p.m."):
        hours, minutes = time.split(":")
        # convert the minutes to a decimal value
        new_minute = float(minutes) / 60
        # add the hours and minutes together
        return float(hours) + new_minute

    elif time.endswith("a.m."):
        time = time.replace("a.m.", "")
        hours, minutes = time.split(":")
        new_minute = float(minutes) / 60
        return float(hours) + new_minute
    elif "p.m." in time:
        # remove the p.m. from the string
        time = time.replace("p.m.", "")
        # split the string into a list divided by the colon
        hours, minutes = time.split(":")
        # convert the hours to a decimal value
        new_minute = float(minutes) / 60
        return float(hours) + new_minute + 12


if __name__ == "__main__":
    main()
