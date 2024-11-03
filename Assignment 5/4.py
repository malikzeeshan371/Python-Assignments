# 4. Update the value of the "age" key to 26.
# Example: {'name': 'John', 'age': 25, 'city': 'New York'} should become {'name': 'John', 'age': 26, 'city': 'New York'}
new_dict = {'name': 'John', 'age': 25, 'city': 'new york'}
new_dict1 = {'age': 26}

new_dict.update(new_dict1)
print(new_dict)
print("\n")
