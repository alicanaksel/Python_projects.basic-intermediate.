# 19.08.2024
# Getting input from user
def user_input():
    first_currency=input("Which money currency do you have? ").lower().strip()
    balance= float(input("How much money do you have? "))
    second_currency= input("Which money currency do you want? ").lower().strip()
    return first_currency,balance,second_currency

 
# Predefined values with nested dictionaries
currency= {
    "euro": {
        "usd": 1.1,
        "gbp": 0.85,
        "tl": 37.20,
    },
    "usd": {
        "euro": 0.91,
        "gpb": 0.77,
        "tl": 33.69,
    },
    "gbp": {
        "euro": 1.17,
        "usd": 1.30,
        "tl": 43.71,
    },
    "tl": {
        "euro":0.027,
        "usd": 0.030,
        "gbp": 0.023,

    }
}

# Main loop to handle currency conversions
while True:
    first_currency,balance,second_currency= user_input()
    if first_currency in currency and second_currency in currency[first_currency]:
        converted_amount = balance * currency[first_currency][second_currency]
        print(f"{balance} {first_currency.upper()} is equal to {converted_amount:.2f} {second_currency.upper()}.")
    else:
        print("Conversion rate not available for the selected currencies.")

    # Ask the user if they want to perform another conversion
    repeat = input("Do you want to convert another currency? (yes/no): ").strip().lower()
    if repeat != "yes":
        break

print("Thank you for using the currency converter!")