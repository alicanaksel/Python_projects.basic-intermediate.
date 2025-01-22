# Quiz grades to total grade
# My way.
FINAL_SCORE= 50 #final score is constant
empty_list=[] #creating an empty list to do some operations on.
print("Welcome to score calculator. Prepare your quiz scores.")
print("PS. you must type 8 quiz score")

# The loop helps us to check that if list contains 8 elements and nonne of the lower than 0 or higher than 10
while True:
    if len(empty_list) <8:
        get_quizz=int(input("Type your quiz: ")) #getting input from the student
        if not 0 < get_quizz <11:
            print("Quizes can be only between 0 and 10")
            break
        empty_list.append(get_quizz) # adding the quiz scores to the empty list
    else:
        break

# this function helps us to determine the two smallest elements in the list and remove them
def determinator():
    smallest=empty_list[0]
    for i in range(1, len(empty_list)):
        if empty_list[i] < smallest:
            smallest= empty_list[i]
    empty_list.remove(smallest)
    
    smallest2= empty_list[0]
    for i in range(1, len(empty_list)):
        if empty_list[i] < smallest2:
            smallest2= empty_list[i]
    empty_list.remove(smallest2)
    return empty_list

# After the removing process we can now sum the quiz scores and print the result.
def calculator(lst):
    determinator()
    quizzes_total= sum(lst)
    print(f"Your total quiz score is {quizzes_total}. ")
    final_score= quizzes_total + FINAL_SCORE
    print(f"Your final score is {final_score}. ")
    return final_score , quizzes_total

#call the function
calculator(empty_list)

'''
# the better version(more improved, cleaner and more efficient)

def get_quiz_scores():
    print("Welcome to the score calculator. Prepare your quiz scores.")
    print("You must enter exactly 8 quiz scores between 0 and 10.")

    quiz_scores = []
    while len(quiz_scores) < 8:
        try:
            score = int(input(f"Enter quiz score {len(quiz_scores) + 1}: "))
            if 0 <= score <= 10:
                quiz_scores.append(score)
            else:
                print("Scores must be between 0 and 10.")
        except ValueError:
            print("Please enter a valid integer.")
    return quiz_scores

def calculate_final_score(scores, base_score=50):
    # Remove the two lowest scores
    sorted_scores = sorted(scores)  # Sort scores in ascending order
    remaining_scores = sorted_scores[2:]  # Exclude the lowest two scores

    # Calculate the total and final score
    quiz_total = sum(remaining_scores)
    final_score = quiz_total + base_score

    print(f"Your total quiz score (excluding the lowest two) is {quiz_total}.")
    print(f"Your final score is {final_score}.")
    return final_score, quiz_total

# Main program
if __name__ == "__main__":
    quiz_scores = get_quiz_scores()
    calculate_final_score(quiz_scores)

'''    
