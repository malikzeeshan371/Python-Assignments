# 10. Create a dictionary with default values using fromkeys method.
# Example: keys = ['Alice', 'Bob', 'Charlie'], default_value = 0 should create {'Alice': 0, 'Bob': 0, 'Charlie': 0}
student_dict2 = {'Alice': 85, 'Bob': 75, 'Charlie': 90}
output_dict = student_dict2.copy()
output_dict.update(dict.fromkeys(output_dict, 0))
print(output_dict)
