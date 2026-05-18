from os import name

from art import logo
from art import vs
from game_data import data
import random

score = 0

def account(details):
    name = details["name"]
    desc = details["description"]
    country = details["country"]
    return f"{name}, a {desc}, {country}."

def check_follower(one, two):
    if one > two:
        return "A"
    else:
        return "B"

print(logo)
account1 = random.choice(data)


should_continue = True
while should_continue:

    account2 = random.choice(data)
    last_one = account2

    print(f"Compare A: {account(account1)}")
    print(vs)
    print(f"Against B: {account(account2)}")

    choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    winner = check_follower(account1["follower_count"], account2["follower_count"])
    if winner == choice:
        score += 1
        print(f"You are correct!, your score is {score}\n")
        account1 = last_one
    else:
        print("\n" * 20)
        print(f"Sorry, you lost, your score is {score}")
        should_continue = False
