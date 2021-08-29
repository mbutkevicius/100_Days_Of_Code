bidding = True
bidders = {}

while bidding:
    name = input("What is your name?\n")
    bid = float(input("What is your bid? \n$"))

    bidders[name] = bid

    still_bidding = input("Are there any other bidders?\n").lower()
    if still_bidding == "no":
        bidding = False

# She put all this in a function but I won't bother because it's a short program
highest_bidder = 0
winner_name = ""
for name in bidders:
    if bidders[name] > highest_bidder:
        highest_bidder = bidders[name]
        winner_name = name

print(f"The winner is {winner_name} with a bid of ${highest_bidder}!")
