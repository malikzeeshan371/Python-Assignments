# 6. Calculate and print the average grade of all students.
# Example: For {'Alice': 85, 'Bob': 92, 'Charlie': 78}, the average grade is 85
student_dict = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
print("The original dict is " + str(student_dict))
res = 0
for value in student_dict.values():
    res += value

res = res/len(student_dict)
print("The average grade is: " + str(res))
print("\n")