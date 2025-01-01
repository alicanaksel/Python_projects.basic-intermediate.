#03.2.4 Leap years.
def is_leap(year):
    if year > 1582:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f"The year {year} is a leap year.")
        else:
            print(f"The year {year} is not a leap year.")
    else:
        print("Please enter a year greater than 1582. The Gregorian correction applies only to years after 1582.")

try:
    get_input = int(input("Enter a year (greater than 1582) to check if it's a leap year: "))
    is_leap(get_input)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
