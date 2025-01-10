
# 2. Write a function `write_list_of_dicts_to_file` that takes a filename and a list of dictionaries,
# and writes each dictionary to a new line in the file in JSON format.
# Example:
# Input: write_list_of_dicts_to_file('data.txt', [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}])
# (Content of 'data.txt' -> '{"name": "Alice", "age": 25}\n{"name": "Bob", "age": 30}\n')
import json

def write_list_of_dicts_to_file(filename , dict1):
    with open(filename, 'w') as file:
        for dictionary in dict1:
            json_string = json.dumps(dictionary)
            file.write(json_string + '\n')
        file.close()


write_list_of_dicts_to_file('Assignment 17/data.txt', [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}])