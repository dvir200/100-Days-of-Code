import os
from calc_art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    calc_on = True
    num1 = float(input("What's the first number?: "))
    for key in operations:
        print(key)
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What's the second number?: "))
    result = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {result}")
    while calc_on is True:
        user_choice = input(f"Type \'y' to continue calculating with {result}, or type \'n' to start a new calculation: ").lower()
        if user_choice == "y":
            save_num = result
            operation_symbol = input("Pick an operation from the line above: ")
            next_num = int(input("What's the next number?: "))
            result = operations[operation_symbol](result, next_num)
            print(f"{save_num} {operation_symbol} {next_num} = {result}")
        elif user_choice == "n":
            calc_on = False
            os.system('cls')
            calculator()

calculator()

