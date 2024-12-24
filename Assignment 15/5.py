
# 5. Write a function `read_lines_from_file` that takes a filename,
# and returns a list of strings, where each string is a line from the file.
# Example:
# Input: read_lines_from_file('lines.txt')
# Output: ['Line 1', 'Line 2', 'Line 3']

def read_lines_from_file(filename):
    file = open(filename , 'r')
    content = file.read()
    print(content)
    
    file.close()

read_lines_from_file('lines1.txt')
