# number to string(0-999)
'''
When printing a check, it is customary to write the check amount
both as a number (“$274.15”) and as a text string (“two hundred
seventy four dollars and 15 cents”).
'''
print("Welcome to the Number to string. You can conver the number < 1000. ")

def digitName(digit):
    if digit == 1: return "one"
    if digit == 2: return "two"
    if digit == 3: return "three"
    if digit == 4: return "four"
    if digit == 5: return "five"
    if digit == 6: return "six"
    if digit == 7: return "seven"
    if digit == 8: return "eight"
    if digit == 9: return "nine"
    return ""

def teenName(number):
    if number == 10: return "ten"
    if number == 11: return "eleven"
    if number == 12: return "twelve"
    if number == 13: return "thirteen"
    if number == 14: return "fourteen"
    if number == 15: return "fifteen"
    if number == 16: return "sixteen"
    if number == 17: return "seventeen"
    if number == 18: return "eighteen"
    if number == 19: return "nineteen"
    return ""

def tensName(number):
    if number == 90: return "ninety"
    if number == 80: return "eighty"
    if number == 70: return "seventy"
    if number == 60: return "sixty"
    if number == 50: return "fifty"
    if number == 40: return "forty"
    if number == 30: return "thirty"
    if number == 20: return "twenty"
    return ""

def numberToString(number):
    # Extract digits
    hundreds = number // 100
    tens_units = number % 100
    tens = (number % 100) // 10
    units = number % 10

    result = ""

    # Handle hundreds
    if hundreds > 0:
        result += digitName(hundreds) + " hundred"

    # Handle tens and units
    if tens_units >= 10 and tens_units <= 19:
        if result:
            result += " "
        result += teenName(tens_units)
    else:
        if tens > 0:
            if result:
                result += " "
            result += tensName(tens * 10)

        if units > 0:
            if result:
                result += " "
            result += digitName(units)

    return result

# Get the number and validate it
while True:
    try:
        number = input("Type your number here: ")
        intNumber = int(number)  # Attempt to convert to an integer

        # Check if the number is in the valid range
        if 0 <= intNumber <= 999:
            print(f"Your number is valid: {intNumber}")
            break  # Exit the loop if valid input
        else:
            print("Your number should be between 0 and 999. Please try again.")
    except ValueError:
        # Catch non-integer inputs
        print("Invalid input! Please enter an integer.")

# Convert the number to string and display it
result = numberToString(intNumber)
print(f"The number {intNumber} in words is: {result}")
