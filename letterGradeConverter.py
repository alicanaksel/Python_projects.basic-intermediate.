# Function to map letter grades to numerical grades
def get_numerical_grade(letter_grade):
    # Dictionary mapping letter grades to numerical values
    grade_mapping = {
        "A": 4.0, "A-": 3.7,
        "B+": 3.3, "B": 3.0, "B-": 2.7,
        "C+": 2.3, "C": 2.0, "C-": 1.7,
        "D+": 1.3, "D": 1.0, "D-": 0.7,
        "F": 0.0
    }
    # Check if the grade exists in the mapping
    if letter_grade in grade_mapping:
        return grade_mapping[letter_grade]
    else:
        return None

# Function to handle user input and process grades
def process_grades():
    while True:
        try:
            # Prompt user for letter grade input
            grade_input = input("Enter your letter grade (e.g., A, B+, C-, etc.): ").strip().upper()

            # Check for valid grade
            numerical_grade = get_numerical_grade(grade_input)
            if numerical_grade is not None:
                print(f"The numerical grade for {grade_input} is {numerical_grade}.")
            else:
                print("Invalid grade entered. Please enter a valid letter grade (e.g., A, B+, C-).")

            # Ask the user if they want to continue
            continue_prompt = input("Do you want to check another grade? (yes/no): ").strip().lower()
            if continue_prompt not in ["yes", "y"]:
                print("Exiting the program. Goodbye!")
                break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Main function to start the program
if __name__ == "__main__":
    print("Welcome to the Grade Translator!")
    process_grades()
