print("Welcome to the calculator! Please separate the numbers with space.")

# Start a loop to allow repeated calculations
while True:
    try:
        def get_input():
            global num1, num2, operator
            num1 = float(input("What is your first number? "))
            operator = input("What is your operator? (Only *, /, +, and -) ")
            num2 = float(input("What is your second number? "))

        get_input()

        def process():
            if operator == "+":
                addition = num1 + num2
                print(f"Result: {addition}")
            elif operator == "-":
                subtraction = num1 - num2
                print(f"Result: {subtraction}")
            elif operator == "*":
                multiplication = num1 * num2
                print(f"Result: {multiplication}")
            elif operator == "/":
                division = num1 / num2
                print(f"Result: {division}")
            else:
                print("Invalid operator!")

        process()

    except (ValueError, ZeroDivisionError):
        print("This app can't calculate this operation.")
    
    # Ask if the user wants to perform another calculation
    again = input("Do you want to perform another calculation? (yes/no): ").lower().strip()
    
    # Exit the loop if the user doesn't want another calculation
    if again != "yes":
        print("Thank you for using the calculator!")
        break
