import random

dice_list = [1, 2, 3, 4, 5, 6]

# Roll the dice 8 times
results = [random.choice(dice_list) for _ in range(8)]

print("Dice rolls:", results)

# Initialize a list to store counts for each dice value (1 to 6)
appearance_counts = [0] * len(dice_list)

# Count occurrences of each number
for result in results:
    appearance_counts[result - 1] += 1  # Use result - 1 for 0-based indexing

# Display the counts
for i, count in enumerate(appearance_counts):
    print(f"{dice_list[i]} appears {count} time(s).")
