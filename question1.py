# Question 1 Task 1 
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse=True)
print("Sorted grades in descending order:", grades)

# Question 1 Task 2
total_grades = sum(grades)
average_grade = total_grades / len(grades)
print("Average grade:", average_grade)

# Question 1 Task 3
grades = ["Failed" if grade < 80 else grade for grade in grades]
print("Updated grades:", grades)