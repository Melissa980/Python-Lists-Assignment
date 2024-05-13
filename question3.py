# Question 3 Task 1 
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
second_week_temperatures = temperatures[7:14]
print("Temperatures for the second week are:", second_week_temperatures)

# Question 3 Task 2 
hot_temperatures = [[temp for temp in temperatures if temp > 100]]
print("Temperatures above 100 are:", hot_temperatures)

# Question 3 Task 3 
temperatures.sort(reverse=True)
temp_day_five_to_ten = temperatures [4:9]
print("Reversed list of temperatures:", temperatures)
print("Temperatures from the 5th to the 10th day of the reversed list:", temp_day_five_to_ten)