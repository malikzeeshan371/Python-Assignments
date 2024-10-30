# Assignment: Working with Dictionaries (Part 2)

# 1. Create a dictionary with student names as keys and their grades as values.
# Example: {'Alice': 85, 'Bob': 92, 'Charlie': 78}
student_dict = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
print(student_dict , end=" ")
print("\n")


# 2. Print the grade of a specific student by name.
# Example: For {'Alice': 85, 'Bob': 92, 'Charlie': 78}, print the grade for "Bob" which is 92
student_dict = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
print(student_dict['Bob'])
print("\n")

# 3. Add a new student and grade to the dictionary.
# Example: {'Alice': 85, 'Bob': 92} should become {'Alice': 85, 'Bob': 92, 'Charlie': 78}
student_dict = {'Alice': 85, 'Bob': 92}
print(student_dict)
student_dict['Charlie'] = 78
print(student_dict)
print("\n")


# 4. Update the grade of an existing student.
# Example: {'Alice': 85, 'Bob': 92} should update Bob's grade to 95, resulting in {'Alice': 85, 'Bob': 95}
student_dict = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
student_dict1 = {'Bob':95}
student_dict.update(student_dict1)
print(student_dict)
print("\n")

# 5. Remove a student from the dictionary.
# Example: {'Alice': 85, 'Bob': 92, 'Charlie': 78} should remove Charlie, resulting in {'Alice': 85, 'Bob': 92}
student_dict = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
del student_dict['Charlie']
print(student_dict)
print("\n")

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

# 7. Find and print the name of the student with the highest grade.
# Example: For {'Alice': 85, 'Bob': 92, 'Charlie': 78}, print "Bob"
student_dict = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
max_val = max(student_dict.values())
max_keys = []
for key in student_dict:
    if student_dict[key] == max_val:
            max_keys.append(key)
print(max_keys)
print("\n")


# 8. Create a nested dictionary to store student information (name, age, grade).
# Example: {'Alice': {'age': 20, 'grade': 85}, 'Bob': {'age': 22, 'grade': 92}}
student_info =  {'Alice': {'age': 20, 'grade': 85}, 'Bob': {'age': 22, 'grade': 92}}
print(student_info)
print("\n")

#
# 9. Print the names of all students who have a grade above 80.
# Example: For {'Alice': 85, 'Bob': 75, 'Charlie': 90}, print "Alice, Charlie"
student_dict2 = {'Alice': 85, 'Bob': 75, 'Charlie': 90}
print(student_dict2)
grade = 80
for k,v in student_dict2.items():
     if v > grade:
          print(student_dict2)
print("\n")


# 10. Create a dictionary with default values using fromkeys method.
# Example: keys = ['Alice', 'Bob', 'Charlie'], default_value = 0 should create {'Alice': 0, 'Bob': 0, 'Charlie': 0}
student_dict2 = {'Alice': 85, 'Bob': 75, 'Charlie': 90}
output_dict = student_dict2.copy()
output_dict.update(dict.fromkeys(output_dict, 0))
print(output_dict)

