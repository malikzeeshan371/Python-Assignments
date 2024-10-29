
# 10. Print all the keys in the dictionary.
# Example: For {'name': 'John', 'age': 25, 'city': 'New York'}, print "name", "age", "city"
my_dict1 = {'name': 'John', 'age': 25, 'city': 'New York'}
for key,value in my_dict1.items():
    print(f"{key}" , end = " ")