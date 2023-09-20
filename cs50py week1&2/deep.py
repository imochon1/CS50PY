answer = input(
    "What is the answer to the great question of life, the universe, and everything? "
)

#remove the whitespace from the answer
answer = answer.strip()

# if answer is 42  or if answer == forty-two or forty tw0, 
if answer == "42":
    print("Yes")
    elif answer == "forty-two" or answer == "Forty Two":
    print("Yes")

else:
    print("No")
