logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
import math

def add(n1, n2):
    """Adding for calculations"""
    return n1 + n2
def subtract(n1, n2):
    """Subtracting for calculations"""
    return n1 - n2
def divide(n1, n2):
    """divide for calculations"""
    return n1 // n2
def multiply(n1, n2):
    """multiply for calculations"""
    return n1 * n2
def power(n1, n2):
    """Power of number"""
    return n1 ** n2
def modular(n1, n2):
    return n1 % n2


operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
    "**": power,
    "%": modular,

}


should_continue = True

def calculator():
    print(logo,"\nWelcome to the Python Calculator")

    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation from above")


    num2 = float(input("What's the next number?: "))

    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'Y' to continue calculations with {answer}, type 'N' to exit or 'n' to start new. : ").casefold() == "y":
        num1 = answer
    else:
        should_continue = False
        calculator()

calculator()
