# Question 4 Task 1
students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

grade_below_eighty = [(name, grade, activity) for name, grade, activity in zip(students, grades, activities) if grade < 80]
for student in grade_below_eighty:
    print(student[0], student[1], student[2])

# Question 4 Task 2
students_approved = [name for name in students if name not in [student[0] for student in grade_below_eighty]]

# Question 4 Task 
print(students_approved)   


