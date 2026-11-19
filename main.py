# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art

print(art.logo)

bids = {}
end_auction = False

while not end_auction:
    name = input("What is your name?: ")
    while True:  # Loop until a valid positive integer is entered
        bid = input("What is your bid?: ")
        if bid.isdigit():
            bid = int(bid)
            break
        else:
            print("Wrong input! Type a number greater than 0")
            continue
    bids[name] = bid
    while True:  # Normalize input to avoid case/whitespace mismatches
        new_bidder = input("Are there any other bidders? (Type 'yes' or 'no'): ").lower().strip()
        if new_bidder not in ["yes", "no"]:
            print("Wrong input! Type 'yes' or 'no'")
            continue
        elif new_bidder == "yes":
            print("\n" * 100)
            break
        else:
            print(bids)
            end_auction = True
            break

highest_bid = 0
winner = ""

for person in bids:
    bid_amount = bids[person]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = person

print(f"The winner of the auction is {winner} with a bid of {highest_bid}")
