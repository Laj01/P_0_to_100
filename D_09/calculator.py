def main():
    calculator()
    
def calculator():
    num1 = float(input('Enter the first number: '))
    for symbol in operators:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input('Pick an operation: ')
        num2 = float(input('Enter the second number: '))
        calc_function = operators[operation_symbol]
        result = calc_function(num1, num2)
        print(f'{num1} {operation_symbol} {num2} = {result}')

        end_of_calc = input('Continue the calculation? "y"\nStart new calculation?    "n"\nExit?                     "e"\n')
        if end_of_calc == 'c':
            num1 = result
        elif end_of_calc == 'n':
            should_continue = False
            calculator()
        else:
            should_continue = False

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


if __name__ == '__main__':
    main()