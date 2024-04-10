from DAY10_ART import logo
print(logo)

def add(n1, n2):
    return n1+n2
def sub(n1, n2):
    return n1-n2
def mul(n1, n2):
    return n1*n2
def div(n1, n2):
    return n1/n2

operations = {
    "+": add, "-": sub, "*": mul, "/": div
}

def calculator():
    num1 = float(input("What is the 1st number: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operations_symbol = input("Pick an symbol: ")
        num2= float(input("Whats the next number?: "))
        calculation = operations[operations_symbol]
        ans=calculation(num1, num2)

        print(f"{num1} {operations_symbol} {num2} = {ans}")

        if input(f"Type 'y' to continue calculating with {ans}: ") == "y":
            num1 = ans
        else: 
            should_continue = False
            calculator()
calculator()

    # operations_symbol = input("Pick another operation: ")
    # num3 = int(input("Whats the next number?: "))
    # calculation = operations[operations_symbol]
    # second_ans= calculation_function(ans, num3)
    # print(f"{ans} {operations_symbol} {num3} = {second_ans}")
    
