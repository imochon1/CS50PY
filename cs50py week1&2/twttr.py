user_input = input("Input: ")
vowels = ["a", "e", "i", "o", "u"]
# if any vowel is in user_input, replace it with an empty string with no space
for vowel in vowels:
    user_input = user_input.replace(vowel, "")
print(user_input)
