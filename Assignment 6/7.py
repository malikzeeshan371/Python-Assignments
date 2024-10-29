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