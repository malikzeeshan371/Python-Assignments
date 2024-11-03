# 6. Check if the key "country" exists in the dictionary.
# Example: For {'name': 'John', 'age': 25, 'city': 'New York'}, print "Key does not exist"
# Example: For {'name': 'John', 'age': 25, 'city': 'New York', 'country': 'USA'}, print "Key exists"
new_dict = {'name': 'John', 'age': 25, 'city': 'new york'}
print(new_dict)

try:
    new_dict['country']
    print("The key exists in the dictionary")
except KeyError as e:
    print("the key does not exist in the dictionary")
print("\n")
