# 10. Write a function `file_statistics` that takes a filename,
# and returns a dictionary with the number of characters, words, and lines in the file.
# Example:
# Input: file_statistics('example.txt')
# (Content of 'example.txt' -> 'This is a file.\nIt has multiple lines.\nAnd some words.')
# Output: {'characters': 49, 'words': 10, 'lines': 3}

def file_statistics(filename):
    number_of_characters = 0
    number_of_words = 0

    with open(filename , 'r') as file:


    #    file = open(filename,'r')
    
    #  lines = len(file.readlines())
    
     data = file.read()
     word_count = data.split()
     number_of_words += len(word_count)

     lines = len(file.readlines())

     for char in data:
          char = number_of_characters
          number_of_characters += char
    print(char)
          

    return{
       'number of words' : number_of_words,
       'no. of lines' : lines,

    }

       
     



input = file_statistics('Assignment 15/filestats.txt')
print(input)
   