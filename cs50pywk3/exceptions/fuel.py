while True:
    fuel = input("Fraction : ")
    try:
        num, den = fuel.split("/")
        num = int(num)
        den = int(den)
        # rounds to the next whole number
        gauge = num / den
        tank = gauge * 100
        rounded = round(tank)

        if num > den:
            raise ValueError
        if num == 0:
            print("E")
            break

        if rounded <= 1:
            print("E")
            break
        elif rounded >= 99:
            print("F")
            break

    except (ZeroDivisionError, ValueError):
        pass
    else:
        print(f"{rounded}%")
        break
