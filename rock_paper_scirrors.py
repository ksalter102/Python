import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to ROCK, PAPER AND SCISSORS."
      "The rules are as follows:\n"
      "ROCK beats SCISSORS\n"
      "SCISSORS beats PAPER\n"
      "PAPER beats ROCK\n")
#
choice = int(input("Choose: 0 for ROCK\n"
                   "\t    1 for PAPER\n"
                   "\t    2 for SCISSORS\n"))

if choice >= 3 or choice < 0:
    print("Invalid number, you lose!")
else:


    computer_choice = random.randint(0, 2)
    print(computer_choice)

    images_computer = [rock, paper, scissors]
    images_computer = images_computer[computer_choice]

    images_user = [rock, paper, scissors]
    images_user = images_user[choice]

    if choice == "0" and computer_choice == 2:
        print("You win!")
        print(images_user)
        print("I chose: ")
        print(images_computer)

    elif computer_choice > choice:
        print("You lose!")
        print(images_user)
        print("I chose: ")
        print(images_computer)

    elif computer_choice == 0 and choice == 2:
        print("You lose!")
        print(images_user)
        print("I chose: ")
        print(images_computer)

    elif choice > computer_choice:
        print("You win!")
        print(images_user)
        print("I chose: ")
        print(images_computer)

    elif computer_choice == choice:
        print("Draw, try again!")
        print(images_user)
        print("I chose: ")
        print(images_computer)

# K. Salter

