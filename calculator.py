def add(x, y):
    # TODO: Implement addition
    pass

def subtract(x, y):
    # TODO: Implement subtraction
    pass

def multiply(x, y):
    # TODO: Implement multiplication
    pass

def divide(x, y):
    # TODO: Implement division
    pass

# Main Calculator
def main():
    print("=== Simple Calculator ===")
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        print(f"Result: {add(num1, num2)}")
    elif operator == "-":
        print(f"Result: {subtract(num1, num2)}")
    elif operator == "*":
        print(f"Result: {multiply(num1, num2)}")
    elif operator == "/":
        print(f"Result: {divide(num1, num2)}")
    else:
        print("Invalid operator")


if __name__ == "__main__":
    main()
