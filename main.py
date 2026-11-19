import art

print(art.logo)

bids = {}
end_auction = False


def find_highest_bidder(bidding_dictionary):
    # Function to find the highest bid.
    highest_bid = 0
    winner = ""
    for person, bid_amount in bidding_dictionary.items():
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = person
    print(
        f"The winner of the auction is ¡¡{winner.title()}!!"
        f" with a bid of ${highest_bid}"
    )


while not end_auction:
    while True:  # Loop while checking if name is already taken.
        name = input("What is your name?: ").lower().strip()
        if not name:
            print("Wrong input! Name cannot be empty")
            continue
        if name in bids:
            print(
                f"The name {name.title()} is already in the auction! "
                f"Try with another name."
            )
            continue
        break
    while True:  # Loop until a valid positive integer is entered
        bid = input("What is your bid?: $ ").strip()
        # Evaluates if the input is a digit and greater than 0
        if bid.isdigit() and int(bid) > 0:
            bid = int(bid)
            break  # breaks the loop
        print("Wrong input! Type a number greater than 0")
        continue  # Repeat loop on invalid input

    bids[name] = bid

    while True:  # User input loop until they enter "yes" or "no"
        new_bidder = (
            input("Are there any other bidders? (Type 'yes' or 'no'): ")
            .lower()
            .strip()
        )  # Normalize input to avoid case/whitespace mismatches
        if new_bidder not in ["yes", "no"]:
            print("Wrong input! Type 'yes' or 'no'")
            continue
        if new_bidder == "yes":
            print("\n" * 100)
        else:
            print(bids)
            find_highest_bidder(bids)
            end_auction = True
        break
