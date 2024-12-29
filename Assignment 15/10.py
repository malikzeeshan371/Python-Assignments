
# 10. Write a function `file_statistics` that takes a filename,
# and returns a dictionary with the number of characters, words, and lines in the file.
# Example:
# Input: file_statistics('example.txt')
# (Content of 'example.txt' -> 'This is a file.\nIt has multiple lines.\nAnd some words.')
# Output: {'characters': 49, 'words': 10, 'lines': 3}

def file_statistics(filename):
    # number_of_characters = 0
    # number_of_words = 0

    # with open(filename , 'r') as file:


    # #    file = open(filename,'r')
    
    # #  lines = len(file.readlines())
    
    #  data = file.read()
    #  word_count = data.split()
    #  number_of_words += len(word_count)

    #  lines = len(file.readlines())

    #  for char in data:
    #       char = number_of_characters
    #       number_of_characters += char
    # print(char)
          

    # return{
    #    'number of words' : number_of_words,
    #    'no. of lines' : lines

    # }

    file = open(filename , 'r')
    lines = file.readlines()
    file.close()
    lines_count = len(lines)

    word_count = 0
    char_count = 0


    for line in lines:
        line_words = line.split()
        word_count += len(line_words)

        char_count += len(line)
    
    return {'characters': char_count, 'words': word_count, 'lines': lines_count}


       
print(file_statistics('Assignment 15/filestats.txt'))
