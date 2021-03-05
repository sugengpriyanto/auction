from replit import clear
from art import logo

print(logo)
print("Welcome to Auction Program")

bids = {}
finished = False

def find_higher(bid_rec):
  higher = 0
  for bidder in bid_rec:
    amount = bid_rec[bidder]
    if amount > higher:
      higher = amount
      winner = bidder
  print(f"The winner is {winner} with a bid of {higher}")

while not finished:
  name = input("What is your name? ")
  brave = int(input("What is your bid? $"))
  bids[name] = brave
  other = input("Are there any other bidders? Type 'yes' or 'no' ")
  if other == "no":
    finished = True
    find_higher(bids)
  elif finished == "yes":
    clear()




