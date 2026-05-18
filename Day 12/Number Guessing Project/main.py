import random

EASY = 10
HARD = 5

def check_answer(guess, num):
    if guess == num:
        print("You got it!")
    elif guess > num:
        print("Too high!")
    elif guess < num:
        print("Too low!")


print("Welcome to the Number Guessing Project")
print("I am thinking of a number between 1 and 100")
num = random.randint(1, 100)

def difficulty():
    if input("Choose a difficulty level: easy or hard: ") == "easy":
        return EASY
    else:
        return HARD

for i in range(difficulty(), 0, -1):
    print(f"You have {i} lives left")
    guess = int(input("Guess a number: "))
    check_answer(guess, num)
    if guess == num:
        break
    elif i == 1:
        print("You are out of lives try again")