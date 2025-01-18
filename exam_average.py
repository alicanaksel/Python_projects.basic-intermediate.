#Step 1 
#compute the grades for multiple students
#outer loop processes each student 
# inner loop processes the specific student's grades
EXAM_TOTAL=0
more_grades= True



while more_grades :
    exam_total = EXAM_TOTAL  # Be careful not to take this as a global unless it'll add up to each other and not gonna calculate the right answer
    exam_number= int(input("How many exam do you want average? "))
    for i in range(exam_number):
        exam_grade=float(input("What is your grade? "))
        exam_total += exam_grade
        exam_average= exam_total / exam_number
    print(f"Your exam's average is {exam_average:.2f}")

    cycle= input("Would you like to repeat the process for someone else?(If yes please type yes/y) ").strip().lower()
    if cycle not in ("yes","y"):
        more_grades = False

print("Thank you for using the exam average calculator!")
