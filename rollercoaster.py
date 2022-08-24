# RIDE ON ROLLERCOASTER
# >120cm in height
# if <= 18 £7
# if > £12


height = int(input("What is your height in cm?\n"))
bill = 0
child = 5
youth = 7
adult = 12

if height > 120:
    age = int(input("How old are you?\n"))
    if age < 12:
        print("Child tickets are £5 ")
        bill += child
    elif age <= 18:
        print("Youth tickets are £7 ")
        bill += youth
    else:
        print("Adult tickets are £12 ")
        bill += adult

    photo = input("Would you like a photo for £3? Y or N\n ".casefold())

    if photo == "Y".casefold():
        # add £3 to bill
        bill += 3
        print(f"Your final bill is £{bill}")

else:
    print("Can't ride")
