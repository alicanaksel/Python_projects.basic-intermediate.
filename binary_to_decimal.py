def validate_reverse_and_convert():
    while True:  # Keep looping until valid input is provided
        binary_number = input("Enter a binary number to validate (or type 'exit' to quit): ").strip()

        if binary_number.lower() == "exit":
            print("Exiting the program. Goodbye!")
            break

        # Check if the input contains only binary digits (0 or 1)
        if all(char in "01" for char in binary_number):
            print("Valid input. All characters are valid binary digits.")

            # Reverse the binary number
            reversed_binary = binary_number[::-1]
            print(f"The reversed binary number is: {reversed_binary}")

            # Convert binary to decimal
            decimal_value = 0
            for i, digit in enumerate(reversed_binary):
                decimal_value += int(digit) * (2 ** i)

            print(f"The decimal equivalent of the binary number {binary_number} is: {decimal_value}")
            break
        else:
            print("Invalid input. Please enter a valid binary number.")

# Call the function
validate_reverse_and_convert()








'''
My first attempt:

def validate_binary():
    while True:  # Keep looping until valid input is provided
        global binary_number
        binary_number = input("Enter a binary number to validate (or type 'exit' to quit): ").strip()        
        
        if binary_number.lower() == "exit":
            print("Exiting the program. Goodbye!")
            break

        for char in binary_number:
            if char not in "01":
                print(f"Invalid input. The character '{char}' is not a valid binary digit.")
                break
        else:
            # This block runs if no invalid characters are found
            print("Valid input. All characters are valid binary digits.")
            break  # Exit the loop after a valid input
        decimal_to_binary()


def decimal_to_binary():
    new_binary= binary_number[::-1]
    return new_binary


'''






