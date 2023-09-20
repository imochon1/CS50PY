months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

while True:
    date = input("Date: ")
    try:
        month, day, year = date.split("/")
        if int(month) >= 1 and int(month) <= 12 and int(day) >= 1 and int(day) <= 31:
            break
    except:
        try:
            prev_month, prev_day, year = date.split(" ")
            normalized_month = prev_month.strip().title()
            for i in range(len(months)):
                if prev_month == months[i]:
                    month = i + 1
            # if day doesnt hacve a comma reject it
            if "," not in prev_day:
                raise ValueError
            day = prev_day.replace(",", "").strip()
            if (
                int(month) >= 1
                and int(month) <= 12
                and int(day) >= 1
                and int(day) <= 31
            ):
                break

        except:
            print()
            pass

formatted_date = f"{year.strip()}-{int(month):02}-{int(day):02}"

print(formatted_date)
