
# 6. Write a function `filter_file_by_word` that takes a filename and a word,
# and writes only the lines that contain the word to a new file.
# Example:
# Input: filter_file_by_word('example.txt', 'keyword', 'filtered.txt')
# (Content of 'example.txt' -> 'This is a line with keyword.\nThis is a line without.\nAnother line with keyword.\n')
# (Content of 'filtered.txt' -> 'This is a line with keyword.\nAnother line with keyword.\n')

def filter_file_by_word(filename,word,newfile):
    with open(filename , 'r') as file:
        lines = file.readlines()

    new_list = []
    idx = 0

    for line in lines:
        if word in line:
         new_list.insert(idx , line)
         idx += 1

    file.close()

    # if len(new_list) == 0:
    #  print('not found')

    # else:
    #    lineLen = len(new_list)
    #    for i in range(lineLen):
    #       end = new_list[i]
    #       print(end)
    

    with open(newfile , 'w') as outfile:
       if len(new_list) == 0:
         print('not found')

       else:
         lineLen = len(new_list)
         for i in range(lineLen):
           end = new_list[i]
           print(end)
           outfile.writelines(end)
    outfile.close()


filter_file_by_word('Assignment 17/original6.txt', 'keyword','Assignment 17/filtered.txt')
