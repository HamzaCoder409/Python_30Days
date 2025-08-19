import math  # For advanced math functions

# ===== Functions =====
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "❌ Error! Division by zero."
    return a / b

def power(a, b):
    return a ** b

def square(a):
    return a ** 2

def square_root(a):
    if a < 0:
        return "❌ Error! Cannot take square root of negative number."
    return math.sqrt(a)

def odd_even(a):
    return "Even" if a % 2 == 0 else "Odd"

# ===== Main Program =====
print("=== Professional Calculator ===")
print("Operations: add, subtract, multiply, divide, power, square, sqrt, odd_even, exit")

while True:
    operation = input("\nEnter operation: ").lower()

    if operation == "exit":
        print("Calculator Closed. Goodbye! 👋")
        break

    # For operations that need 2 numbers
    if operation in ["add", "subtract", "multiply", "divide", "power"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operation == "add":
            print(" Result:", add(num1, num2))
        elif operation == "subtract":
            print(" Result:", subtract(num1, num2))
        elif operation == "multiply":
            print(" Result:", multiply(num1, num2))
        elif operation == "divide":
            print(" Result:", divide(num1, num2))
        elif operation == "power":
            print(" Result:", power(num1, num2))

    # For operations that need 1 number
    elif operation in ["square", "sqrt", "odd_even"]:
        num = float(input("Enter number: "))

        if operation == "square":
            print(" Result:", square(num))
        elif operation == "sqrt":
            print(" Result:", square_root(num))
        elif operation == "odd_even":
            print(" Result:", odd_even(int(num)))

    else:
        print("❌ Invalid operation! Please try again.")
