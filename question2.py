# Question 2 Task 1
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

common_students = set(submitted) & set(attended)
print("Students who both submitted assignments and attended class:", list(common_students))

# Question 2 Task 2
if set(submitted) == set(attended):
    print("The two lists are identical in terms of their content.")
else:
    print("The two lists are not identical in terms of their content.")

# Question 2 Task 3
attended.remove(attended[3])    
attended.remove(attended[1])
print("Updated attended list:", attended)