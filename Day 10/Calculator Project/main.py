from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

def calculate():
    print(logo)
    should_continue = True
    firstnum = int(input("What is your first number?: "))

    while should_continue:
        operand = input("What is your operand? (+, -, *, /): ")
        print(operations.keys())
        secondnum = int(input("What is your second number?: "))
        result = operations[operand](firstnum, secondnum)
        print(f"Your result is: {result}")
        next = input("Would you like to continue working with the previous result? (yes/no): ")

        if next == "yes":
            firstnum = result
        else:
            should_continue = False
            print("\n" * 100)
            calculate()

calculate()


