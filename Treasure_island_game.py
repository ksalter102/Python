# TREASURE ISLAND


print(''' _
| |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ __ ___   __ _ _ __
| __| '__/ _ \/ _` / __| | | | '__/ _ \ '_ ` _ \ / _` | '_ \
| |_| | |  __/ (_| \__ \ |_| | | |  __/ | | | | | (_| | |_) |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_| |_| |_|\__,_| .__/
                                                      | |
                                                      |_|    ''')

name = input("What's your name?\n".strip().title())

print(f"Welcome to Treasure Island {name}.\nGo find that TREASURE.")
option_1 = input(f"{name}\nYou have a choice, you can do RIGHT into a cave.\n"
                 f"Or you can go left through the forest.\n"
                 f"Will you go LEFT or RIGHT?\n")

if option_1 == "left".casefold():
    print("-" * 80)
    option_2 = input(f"Great choice {name}, you have avoided a trap!\n"
                     f"However you have now reached a river with STRONG waters.\n"
                     f"What will you do next?\nSWIM or WAIT? ")

    if option_2 == "Wait".casefold():
        print("-" * 80)
        option_3 = input(f"Well done {name}, you have avoided Crocodile infested "
                         f"waters\nYou have spotted a house with two doors.\n"
                         f"one RED and one BLUE.\nWhich door will you choose?\n"
                         f"RED or BLUE?")

        if option_3 == "Blue".casefold():
            print(f"Well done {name}, YOU WIN!!")
        else:
            print("You fell through a trap door!\tGAME OVER")
    else:
        print("You were eaten by a Crocodile!\tGAME OVER")
else:
    print("You got lost down a dead end!\tGAME OVER")
