# 8. Write a function `find_and_replace_in_file` that takes a filename, a target string, and a replacement string,
# and replaces all occurrences of the target string with the replacement string in the file.
# Example:
# Input: find_and_replace_in_file('example.txt', 'old', 'new')
# (Content of 'example.txt' before -> 'This old house.')
# (Content of 'example.txt' after -> 'This new house.')

def find_and_replace_in_file(filename ,target_word, replacement_word):
    target_data = target_word
    replaced_word = replacement_word

    with open(filename , 'r') as file:
        data = file.read()
        data = data.replace(target_data , replaced_word)

    with open(filename , 'w') as file:
        file.write(data)
    print('replaced')
    
find_and_replace_in_file('Assignment 15/findandreplacefile.txt', 'new', 'my')

