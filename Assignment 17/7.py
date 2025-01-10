
# 7. Write a function `count_word_occurrences` that takes a filename and a word,
# and returns the number of occurrences of the word in the file.
# Example:
# Input: count_word_occurrences('example.txt', 'word')
# (Content of 'example.txt' -> 'word1 word2 word word3 word word')
# Output: 3

def count_word_occurrences(filename , word_occur):

    with open(filename , 'r') as file:
        word_count = 0

        lines = file.readlines()
        file.close()
        for line in lines:
            words = line.split()
            for i in words:
                if(i == word_occur):
                    word_count += 1
    print(word_count)


                
                
            
count_word_occurrences('Assignment 17/wordoccurrences.txt', 'word')
