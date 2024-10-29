
# 4. Update the grade of an existing student.
# Example: {'Alice': 85, 'Bob': 92} should update Bob's grade to 95, resulting in {'Alice': 85, 'Bob': 95}
student_dict = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
student_dict1 = {'Bob':95}
student_dict.update(student_dict1)
print(student_dict)
print("\n")