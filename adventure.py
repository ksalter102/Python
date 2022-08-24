available_exits = ["north", "south", "east", "west".casefold()]

chosen_exit = ""
while chosen_exit.casefold() not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit.casefold() == "quit":
        print("Game over")
        break

else:
    print("Arent you glad you escaped")