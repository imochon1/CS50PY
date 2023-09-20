# students = ["Herm", "Harry", "Ron", "Draco"]
# houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
# for student in students:
#    print(student)
# for i in range(len(students)):  # len() is a function that returns the length of a list
#    print(i, students[i])


# Dictionaries or dicts ( dict ) is a data structure that stores data in key-value pairs
# students = {
#    "Hermione": "Gryffindor",
#    "Harry": "Gryffindor",
#    "Ron": "Gryffindor",
#    "Draco": "Slytherin",
#    "Luna": "Ravenclaw",
#    "Cedric": "Hufflepuff",
# }

# for student in students:
#    print(
#        student, students[student], sep=", "
#    )  # students[student] is the value of the key student

# stud = input("Enter a student: ")

# print(students[stud])
students = [
    {"name": "Hermione", "house": "Gryffindor", "Patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "Patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "Patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "Patronus": None},
    {"name": "Luna", "house": "Ravenclaw", "Patronus": "Hare"},
    {"name": "Cedric", "house": "Hufflepuff", "Patronus": None},
]

for student in students:
    print(student["name"], student["house"], student["Patronus"], sep=", ")
