# PIZZA ORDER

name = input("Welcome to Keelan's Pizza Deliveries!\nWhat's your name?\n")
size = input("What what pizza do you want?\n S, M, L\t")
add_pepperoni = input("Do you want pepperoni?\n Y, N\t")
extra_cheese = input("Do you want extra cheese?\n Y, N\t")

small_pizza = 15
medium_pizza = 20
large_pizza = 25
pepperoni_small = 2
pepperoni_large = 3
cheese = 1
price = 0

if size == "S".casefold():
    price += small_pizza
elif size == "M".casefold():
    price += medium_pizza
else:
    price += large_pizza

if add_pepperoni == "Y".casefold():
    if size == "S":
        price += pepperoni_small
    else:
        price += pepperoni_large

if extra_cheese == "Y".casefold():
    price += cheese

print("Thanks {}, your final bill will be £{}".format(name, price))