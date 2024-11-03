# 9. Print the names of all students who have a grade above 80.
# Example: For {'Alice': 85, 'Bob': 75, 'Charlie': 90}, print "Alice, Charlie"
student_dict2 = {'Alice': 85, 'Bob': 75, 'Charlie': 90}
print(student_dict2)
grade = 80
for k, v in student_dict2.items():
    if v > grade:
        print(student_dict2)
print("\n")
