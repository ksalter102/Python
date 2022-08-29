import os

# Clearing the Screen
os.system('cls')

def cls():
    print('\n' * 50) #TODO DELETE

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record): #bidding_record = {"keelan": 145, "El": 254}
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of £{highest_bid}")



while not bidding_finished:
    name = input("What is your name?: ").strip().title()
    bid = int(input(f"{name}, what is your bid? £").strip())
    bids[name] = bid
    should_continue = input(f"{name}, are there any other bidders?: Y / N").strip().lower()
    if should_continue == "n":
        bidding_finished = True
        find_highest_bidder(bids)
        break
    elif should_continue == "y":
        cls()


