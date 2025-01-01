#03.2.6 Taxation.
def calculate_tax(income, marital_status):
    if marital_status == "unmarried":
        if 0 < income <= 8000:
            tax = income * 10 / 100
        elif 8000 < income <= 32000:
            tax = 800 + ((income - 8000) * 15 / 100)
        elif income > 32000:
            tax = 4400 + ((income - 32000) * 25 / 100)
        else:
            print("Income must be greater than 0.")
            return
    elif marital_status == "married":
        if 0 < income <= 16000:
            tax = income * 10 / 100
        elif 16000 < income <= 64000:
            tax = 1600 + ((income - 16000) * 15 / 100)
        elif income > 64000:
            tax = 8800 + ((income - 64000) * 25 / 100)
        else:
            print("Income must be greater than 0.")
            return
    else:
        print("Invalid marital status. Please enter 'married' or 'unmarried'.")
        return

    print(f"Your tax is ${tax:.2f}.")

# Input handling
try:
    marital_status = input("Are you married? (yes/no or y/n): ").lower().strip()
    if marital_status in ["yes", "y"]:
        marital_status = "married"
    elif marital_status in ["no", "n"]:
        marital_status = "unmarried"
    else:
        raise ValueError("Invalid marital status.")

    income = float(input("What is your income? "))
    if income < 0:
        raise ValueError("Income cannot be negative.")

    # Calculate tax
    calculate_tax(income, marital_status)

except ValueError as e:
    print(f"Error: {e}")
