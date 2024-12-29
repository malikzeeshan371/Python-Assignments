
# 5. Write a function `read_lines_from_file` that takes a filename,
# and returns a list of strings, where each string is a line from the file.
# Example:
# Input: read_lines_from_file('lines.txt')
# Output: ['Line 1', 'Line 2', 'Line 3']

def read_lines_from_file(filename):
    # new_ouput = []
    file = open(filename , 'r')
    content = file.readlines()

    
  
    file.close()

    return [line.strip() for line in content]



read_from_file = read_lines_from_file('lines1.txt')
print(read_from_file)
