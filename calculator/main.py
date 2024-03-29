from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def power(n1, n2):
    return n1**n2


def modulus(n1, n2):
    return n1 % n2


def floor_division(n1, n2):
    return n1 // n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": power,
    "%": modulus,
    "//": floor_division,
}


def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(f"{symbol} --> {operations[symbol].__name__}")
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation : ")
        num2 = float(input("What's the second number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        should_continue_flag = input(
            f"Type 'y' to continue calculating with {answer}, type .exit to exit ,or type 'n' to start a new calculation.: "
        )
        if should_continue_flag == "y":
            num1 = answer
        elif should_continue_flag == "n":
            calculator()
        else:
            should_continue = False


calculator()
