
# 5. Write a function `reverse_file_content` that takes a filename,
# and writes the content of the file in reverse order to a new file.
# Example:
# Input: reverse_file_content('example.txt', 'reversed.txt')
# (Content of 'example.txt' -> 'Line 1\nLine 2\nLine 3\n')
# (Content of 'reversed.txt' -> 'Line 3\nLine 2\nLine 1\n')

def reverse_file_content(filename, output_file):
    with open(filename, 'r') as file:
        lines = file.readlines()
    file.close()
    reversed_lines = lines[::-1]

    with open(output_file , 'w') as outputfile:
        outputfile.writelines(reversed_lines)
    outputfile.close()

    # print(reversed_lines)


reverse_file_content('Assignment 17/original5.txt','Assignment 17/reversed.txt')
