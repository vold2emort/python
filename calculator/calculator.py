from art import logo


def add(n1, n2):
    return n1+n2


def subtract(n1, n2):
    return n1-n2


def multiply(n1, n2):
    return n1*n2


def divide(n1, n2):
    return n1/n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    num1 = float(input("Enter first number: "))
    should_continue = True
    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("Enter second number: "))
        calculation = operations[operation_symbol]
        answer = calculation(num1, num2)
        print(answer)
        if input(f"Type 'y' t to continue calculating , or 'n' to start new calculation\n") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
