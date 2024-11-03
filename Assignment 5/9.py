# 9. Merge two dictionaries into one. Example: d1 = {'name': 'John', 'age': 25}, d2 = {'city': 'New York',
# 'country': 'USA'} should become {'name': 'John', 'age': 25, 'city': 'New York', 'country': 'USA'}
dict_1 = {'name': 'John', 'age': 25}
dict_2 = {'city': 'new york', 'country': 'USA'}
dict_1.update(dict_2)
print(dict_1)
print("\n")
