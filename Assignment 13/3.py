# 3. Write a function `calculate_average` that takes a list of grades and returns the average grade.
# Example:
# Input: calculate_average([90, 80, 70])
# Output: 80.0
def calculate_average(grades):
    total_marks = 0
    for grade in grades:
     total_marks += grade
    return total_marks/len(grades)
average = calculate_average([90,80,70])
print("The average is: " , average)
print("\n")
