
# 4. Write a function `write_lines_to_file` that takes a filename and a list of strings,
# and writes each string to a new line in the file.
# Example:
# Input: write_lines_to_file('lines.txt', ['Line 1', 'Line 2', 'Line 3'])
# (Content of 'lines.txt' -> 'Line 1\nLine 2\nLine 3\n')

def write_lines_to_file(filename , line_of_messages):
    #filename = 'lines.txt' 
    #line_of_messages =  ['Line 1', 'Line 2', 'Line 3']
     file = open(filename , 'w')
     for line in line_of_messages:
        file.write(line + '\n') 
    
     file.close()

    




write_lines_to_file('lines1.txt', ['Line 22', 'Line 5', 'Line 6'])

