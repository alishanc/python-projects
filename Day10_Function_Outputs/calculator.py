from art import logo


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

    num1 = float(input("What is the first number? "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the second number? "))
        calc_func = operations[operation_symbol]
        answer = calc_func(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation.: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()
            # RECURSION # Starts the function again from first number
            # Ensure conditon to require re-calling the function


calculator()
