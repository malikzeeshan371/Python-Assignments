# 7. Create a nested dictionary from a list of tuples. Example: tuples = [('Alice', 'Math', 90), ('Alice', 'Science',
# 85), ('Bob', 'Math', 78), ('Bob', 'Science', 82)] should create {'Alice': {'Math': 90, 'Science': 85},
# 'Bob': {'Math': 78, 'Science': 82}}
tups = [('Alice', 'Math',90), ('Alice','Science',85),('Bob','Math',78),('Bob', 'Science',82)]
nested_dict = {}
for name,subject,score in tups:
    if name not in nested_dict:
        nested_dict[name] = {}
    nested_dict[name][subject] = score
print(nested_dict)
print('\n')
