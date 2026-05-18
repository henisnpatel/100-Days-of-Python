MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

collected_money = 0

def check(flavour):
    if resources["water"] < flavour["water"]:
        print("Sorry not enough water")
    elif resources["coffee"] < flavour["coffee"]:
        print("Sorry not enough coffee")
    elif "milk" in flavour and resources["milk"] < flavour["milk"]:
        print("Sorry not enough milk")
    else:
        resources["water"] -= flavour["water"]
        resources["coffee"] -= flavour["coffee"]
        if "milk" in flavour:
            resources["milk"] -= flavour["milk"]

def process_coins(quarters, dimes, nickles, pennies, flavour, profit):
    money = quarters * 0.25
    money += dimes * 0.10
    money += nickles * 0.05
    money = int(money) + pennies * 0.01
    if money < flavour["cost"]:
        print("Sorry not enough money")
        return profit
    else:
        money -= flavour["cost"]
        print(f"You have remaining {money}")
        profit += flavour["cost"]
        return profit

should_continue = True

while should_continue:
    make = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if make == "off":
        should_continue = False
    elif make == "report":
        for key in resources:
            print(f"{key}: {resources[key]}")
        print(f"Profit: {collected_money}")
    else:
        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickles = int(input("How many nickles? "))
        pennies = int(input("How many pennies? "))
        check(MENU[make]["ingredients"])
        collected_money = process_coins(quarters, dimes, nickles, pennies, MENU[make], collected_money)







