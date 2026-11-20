#add
def add(x, y):
    # TODO: 
    pass

def subtract(x, y):
    # TODO: 
    pass

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

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
