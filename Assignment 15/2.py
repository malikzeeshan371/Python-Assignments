
# 2. Write a function `read_message_from_file` that takes a filename,
# and returns the content of the file as a string.
# Example:
# Input: read_message_from_file('message.txt')
# Output: 'Hello, World!'

def read_message_from_file(filename):
    with open(filename , 'r') as file:
       contents =  file.read()
    file.close()
    print(contents)

read_message_from_file('Assignment 15/message.txt')
