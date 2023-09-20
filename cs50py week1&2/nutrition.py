fruit = input("Enter a fruit: ").title()
print(fruit)

fruit_list = [
    {
        "name": "Apple",
        "calories": 130,
    },
    {
        "name": "Avocado",
        "calories": 50,
    },
    {
        "name": "Banana",
        "calories": 110,
    },
    {
        "name": "Canteleoupe",
        "calories": 50,
    },
    {
        "name": "Grapefruit",
        "calories": 60,
    },
    {
        "name": "Grapes",
        "calories": 90,
    },
    {
        "name": "Sweet Cherries",
        "calories": 100,
    },
    {
        "name": "Kiwifruit",
        "calories": 90,
    },
    {
        "name": "Pear",
        "calories": 100,
    },
]


for fruit_dict in fruit_list:
    if fruit_dict["name"] == fruit:
        print(fruit_dict["calories"])
        break
