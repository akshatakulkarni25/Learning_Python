import os
from art import logo
#HINT: You can call clear() to clear the output in the console.
def find_highest_bidder(bidder_details):
  highest_bid = -1
  higgest_bidder = ""
  for bid in bidder_details:
    if(bidder_dict[bid] > highest_bid):
      highest_bid=bidder_dict[bid]
      higgest_bidder=bid
  os.system('clear')
  print(f"The winner is {higgest_bidder} with a bid of Rs{highest_bid}")

print(logo)
print("Welcome to the secret aution program.")
bidder_dict ={}
more_bidders= 1
while(more_bidders):
  bidder_name = input("What is your name?: ")
  bidder_bid = int(input("What's your bid?: Rs"))
  bidder_dict[bidder_name]=bidder_bid
  more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if(more_bidders == "yes"):
    more_bidders=1
    os.system('clear')
  else:
    more_bidders=0
find_highest_bidder(bidder_details=bidder_dict)

  

