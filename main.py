# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

bids = {

}

while True:
    new_bidder = ""
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    bids[name] = bid
    new_bidder = input("Are there any other bidders?: ").lower()
    if new_bidder == "yes":
        print("\n" * 100)
        continue
    else:
        print(bids)
        break
