from art import logo
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def calculate_score(cardlist):
    if sum(cardlist) == 21 and len(cardlist) == 2:
        return 0
    return sum(cardlist)

def deal_card():
    player.append(random.choice(cards))
    player.append(random.choice(cards))
    computer.append(random.choice(cards))

def computercard():
    while calculate_score(computer) <= 16:
        computer.append(random.choice(cards))

def check(pnum, cnum):
    if pnum == 0 and cnum != 0:
        return "You got blackjack"
    elif pnum < cnum <= 21:
        return "you lose"
    elif pnum > 21:
        return "you busted you lose"
    elif pnum > cnum or cnum > 21:
        return "you win"
    else:
        return "draw"

def play():
    deal_card()
    should_continue = True
    while should_continue:
        print(f"Your cards: {player}, current score: {calculate_score(player)}")
        print(f"Computer's first card: {calculate_score(computer)}")

        if calculate_score(player) > 21:
            should_continue = False
        else:
            keepgoing = input("Type 'y' to get another card, type 'n' to pass: ")
            if keepgoing == 'y':
                player.append(random.choice(cards))
                if 11 in player and sum(player) > 21:
                    player.remove(11)
                    player.append(1)
            else:
                should_continue = False

    if not calculate_score(player) > 21:
        computercard()
        print(f"Computer's final hand: [{computer}], final score: {calculate_score(computer)}")

    print(check(calculate_score(player), calculate_score(computer)))

interest = input("Welcome to the game! you like to play blackjack y/n: ")
while interest == "y":
    player = []
    computer = []
    print(logo)
    play()
    interest = input("you like to blackjack again y/n: ")





