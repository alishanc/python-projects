import os
# Clearing the Screen
# os.system('cls')
from art import logo
print(logo)

auction_list = {}


def add_bids():
    bidder = input("What is the bidder's name?\n")
    price = int(input("Place your bid\n"))
    auction_list[bidder] = price # bidder = key | price = value
    if input("Are there others?\n") == "yes":
        os.system('cls')
        add_bids()
    else:
        print(auction_list)


add_bids()

winning_bidder = max(auction_list, key=auction_list.get)
print("The winning bidder is:", winning_bidder)
