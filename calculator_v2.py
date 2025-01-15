# Welcome to the calculator
from math import sqrt

def perform_operation(number, operation, number_2=None):
    """Performs the specified operation and returns the result."""
    if operation == "+":
        return number + number_2
    elif operation == "-":
        return number - number_2
    elif operation == "*":
        return number * number_2
    elif operation == "/":
        if number_2 != 0:
            return number / number_2
        else:
            print("Division by zero is undefined.")
            return number  
    elif operation == "**":
        return number ** number_2
    elif operation == "%":
        if number_2 != 0:
            return number % number_2
        else:
            print("Modulus by zero is undefined.")
            return number  
    elif operation == "//":
        if number_2 != 0:
            return number // number_2
        else:
            print("Floor division by zero is undefined.")
            return number  
    elif operation == "sqrt":
        if number >= 0:
            return sqrt(number)
        else:
            print("Square root of a negative number is undefined.")
            return number  
    else:
        print("Invalid operation! Please choose from (+, -, *, /, **, %, //, sqrt).")
        return number  

# Main Program
try:
    number = float(input("What is your number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

while True:
    operation = input("Please enter a valid operation (+, -, *, /, **, %, //, sqrt) or type 'exit' to quit: ").strip()

    if operation.lower() == "exit":
        print("Thank you for using the calculator!")
        break

    # Handle operations requiring a second number
    number_2 = None
    if operation in ("+", "-", "*", "/", "**", "%", "//"):
        try:
            number_2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

    number = perform_operation(number, operation, number_2)

    print(f"The result is: {number:.2f}")
