# 03.1.3 Strings and substrings
dnaLETTERS = ["A", "C", "G", "T"]
print("DNA letters are ", dnaLETTERS)

# Input for the long DNA sequence
while True:
    long_sequence = input("Type the 20 characters long DNA sequence: ").upper()
    if len(long_sequence) == 20 and all(char in dnaLETTERS for char in long_sequence):
        break
    else:
        print("The long sequence DNA should have 20 valid characters (A, C, G, T).")

# Input for the short DNA sequence
while True:
    short_sequence = input("Type the 3 characters short DNA sequence: ").upper()
    if len(short_sequence) == 3 and all(char in dnaLETTERS for char in short_sequence):
        break
    else:
        print("The short sequence DNA should have 3 valid characters (A, C, G, T).")

# I. Check if the short sequence is in the long sequence
is_present = short_sequence in long_sequence

# II. Find the first occurrence position (1-based index)
if is_present:
    first_position = long_sequence.find(short_sequence) + 1  # Add 1 to make it 1-based index
else:
    first_position = -1  # Not found

# III. Count the occurrences of the short sequence in the long sequence
count_occurrences = long_sequence.count(short_sequence)

# Display Results
print("\nResults:")
print(f"1. Is the short sequence present in the long sequence? {'Yes' if is_present else 'No'}")
if is_present:
    print(f"2. The short sequence first appears at position: {first_position}")
else:
    print("2. The short sequence is not present in the long sequence.")
print(f"3. The short sequence appears {count_occurrences} time(s) in the long sequence.")
