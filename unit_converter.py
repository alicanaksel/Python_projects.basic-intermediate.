def user_input():
    print("Available units for conversion:")
    print("From units (choose one): ml, l, g, kg, mm, cm, m, km")
    print("To units (choose one): fl, oz, gal, lb, in, ft, mi")
    first_unit = input("Which unit would you like to convert from? ").strip().lower()
    quantity = float(input("Enter the quantity of the unit: "))
    second_unit = input("Which unit would you like to convert to? ").strip().lower()
    return first_unit, quantity, second_unit

conversions= {
    "ml": {
        "fl": 0.033814,
        "gal": 0.00026417,
    },
    "l":{
        "fl": 33.814,
        "gal":  0.264172,
    },
    "g":{
        "oz": 0.035274,
        "lb": 0.00220462262,
    },
    "kg":{
        "oz": 35.274,
        "lb": 2.20462,
    },
    "mm":{
        "in": 0.0393701,
        "ft": 0.0032808399,
        "mi": 6.21371192 * 10 ** -7,
    },
    "cm":{
        "in": 0.393701,
        "ft": 0.032808399,
        "mi": 6.21371192 * 10 ** -6,
    },
    "m":{
        "in": 39.3701,
        "ft": 3.28084,
        "mi": 0.621371,
    },
    "km": {
        "in": 39370.1,
        "ft": 3280.84,
        "mi": 0.621371,
    },
}


while True:
    first_unit, quantity, second_unit= user_input()
    if first_unit in conversions and second_unit in conversions[first_unit]:
        converted_quantity= quantity * conversions[first_unit][second_unit]
        print(f"{quantity} {first_unit} is equal to {converted_quantity:.2f} {second_unit} .")
    else:
        print("Conversion unit is not available for the selected units.")
    
    repeat= input("Do you want to convert another unit? (yes/no): ").strip().lower()
    if repeat != "yes":
        break

print("Thank you for using the unit converter!")
