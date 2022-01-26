#exercise 1

user_funds = 10.31
item_price = 10.32

if item_price < user_funds:
    print("You have enough money!")
if item_price == user_funds:
    print("You have the precise amount of money")
if item_price > user_funds:
    print("Sorry you dont have enough money")

#exercise 2
def product(n):
    total = 1
    for n in n:
        total *= n
    return total

print(product([4,4,5]))