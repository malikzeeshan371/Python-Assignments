# 7. Write a function `count_words_in_file` that takes a filename,
# and returns the number of words in the file.
# Example:
# Input: count_words_in_file('words.txt')
# (Content of 'words.txt' -> 'This is a file with some words.')
# Output: 7

def count_words_in_file(filename):
    number_of_words = 0
    file = open(filename , 'r')
    contents =  file.read()
    lines = contents.split()

    number_of_words += len(lines)
    return number_of_words
    file.close()
input = count_words_in_file('Assignment 15/wordcount.txt')
print(input)



