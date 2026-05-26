from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


should_continue = True

while should_continue:
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        should_continue = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink and coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)