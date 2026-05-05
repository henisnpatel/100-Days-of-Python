# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import logo

print(logo)
bids = {}
should_continue = True
while should_continue:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    bids[name] = bid
    players = input("Is there more players?: ").lower()
    print("\n" * 100)
    if players == "no":
        should_continue = False


top = 0
winner = ""
for key in bids.keys():
    amount = bids[key]
    if amount > top:
        top = amount
        winner = key

print(f"{winner} has bidded {top} and won the auction.")
