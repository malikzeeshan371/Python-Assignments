# 9. Write a function `remove_empty_lines` that takes a filename,
# and removes all empty lines from the file.
# Example:
# Input: remove_empty_lines('lines.txt')
# (Content of 'lines.txt' before -> 'Line 1\n\nLine 2\n\nLine 3\n')
# (Content of 'lines.txt' after -> 'Line 1\nLine 2\nLine 3\n')

def remove_empty_lines(filename):
    file = open(filename , 'r+')
    for lines in file:
        if lines.strip():
            file.write(lines)

    file.close()


remove_empty_lines('lines1.txt')

