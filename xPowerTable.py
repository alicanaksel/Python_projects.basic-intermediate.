# The power table for elementary schools

# Defining the Constants
# NMAX: Maximum power to calculate (columns in the table)
# XMAX: Maximum base number (rows in the table)
NMAX = 4  # Define the maximum power (x^1 to x^4)
XMAX = 10  # Define the maximum base number (1 to 10)

# Creating a loop for the headers
# This loop prints the headers x^1, x^2, ..., up to x^NMAX
for n in range(1, NMAX + 1):  
    result = f"x^{n}"  # Format the header as "x^n"
    print(f"{result:<8}", end="")  # Print each header left-aligned with a width of 8 spaces

# Print the rows of the table
# Outer loop iterates over each base number from 1 to XMAX
for x in range(1, XMAX + 1):
    print()  # Move to the next line for each new base number
    # Inner loop calculates and prints powers of the base number
    for i in range(1, NMAX + 1):
        number = x ** i  # Calculate x^i (base x raised to the power of i)
        print(f"{number:<8}", end="")  # Print each power left-aligned with a width of 8 spaces
