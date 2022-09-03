student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇

'''We use the below 'student variable in the for loop because:
In Python, when looping through a dictionary, the looped variable only returns the KEY
    and not the whole 'key: value' pair.
We can expect that the student variable will reference the KEY in the dictionary above
    i. e. Harry, Draco etc etc...
    When in doubt - PRINT
    print(student)
'''
for student in student_scores:
    # print(student)
    # define a new variable for the dict keys retrieved from the student variable called in for loop
    score = student_scores[student]
    if score > 90:  # once this if statement triggers, it skips all the following elifs
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)
