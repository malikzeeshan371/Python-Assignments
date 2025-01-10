
# 3. Write a function `read_file_into_dict` that takes a filename where each line is a JSON string of a dictionary,
# and returns a list of dictionaries.
# Example:
# Input:
# (Content of 'data.txt' -> '{"name": "Alice", "age": 25}\n{"name": "Bob", "age": 30}\n')
# Output: [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]

import json

def read_file_into_dict(filename):
    data_read = []
    with open(filename , 'r') as file:
        
        for lines in file:
            data_read.append(json.loads(lines))
    file.close()
    return data_read
  
    

print( read_file_into_dict('Assignment 17/data.txt'))