amount_due = 50
print("Amount Due:", amount_due)


while amount_due > 0:
    coin = int(input("Insert Coin: "))
    if coin in [5, 10, 25]:
        amount_due -= coin
        print("Amount Due:", amount_due)
    else:
        print("Amount Due:", amount_due)


change = abs(amount_due)
print("Change Owed:", change)
