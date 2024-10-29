# 8. Create a dictionary from two lists: one with keys and one with values.
# Example: keys = ['name', 'age'], values = ['John', 25] should become {'name': 'John', 'age': 25}
list1 = ['name', 'age']
list2 = ['John' , 25]

res = {}
for key in list1:
    for value in list2:
        res[key] = value
        list2.remove(value)
        break
print("The result is " + str(res))
print("\n")