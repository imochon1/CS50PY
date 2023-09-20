# import random IMPORT COMENTADO
# To import the choice function from the random module, we use the from keyword followed by the module name (random), then the import keyword, and finally the function name (choice). We can also import multiple functions from the same module by separating them with commas.
from random import choice, randint, shuffle

# choice is a function that takes a list as an argument and returns a random element from the list, in this case either "Heads" or "Tails"
coin = choice(["Heads", "Tails"])
# print("You flipped a coin and got: " + coin)

number = randint(1, 10)
# print("Your lucky number is: " + str(number))

cards = ["jack", "queen", "king", "ace"]
shuffle(cards)

for card in cards:
    print(card)
