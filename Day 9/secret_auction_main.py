import os
import secret_auction_art

def add_bidder(name, bid):
  bidders_dic[name] = bid

def find_highest_bidder(dic):
  name_of_bidder = ""
  highest = 0
  for key in bidders_dic:
    if bidders_dic[key] > highest:
      name_of_bidder = key
      highest = bidders_dic[key]
  
  print(f"The winner is {name_of_bidder} with a bid of ${str(highest)}.")


bidders_dic = {}
print(secret_auction_art.logo)
print("Welcome to the secret auction program.")

auction_going = True

while auction_going == True:
  user_name = input("What is your name?: ")
  user_bid = int(input("What is your bid?: $"))
  add_bidder(user_name, user_bid)
  more_bidders = input("Are there any other bidders?: type \'yes' or \'no'. ")
  if more_bidders.lower() == "yes":
    os.system('cls')
  elif more_bidders.lower() == "no":
    auction_going = False
    os.system('cls')

find_highest_bidder(bidders_dic)