# 7. Loop through the dictionary and print all key-value pairs.
# Example: For {'name': 'John', 'age': 25, 'city': 'New York'}, print "name: John", "age: 25", "city: New York"
new_dict = {'name': 'John', 'age': 25, 'city': 'new york'}
for key, value in new_dict.items():
    print(f"{key}:{value}", end=" ")
print("\n")
