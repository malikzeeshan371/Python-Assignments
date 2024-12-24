# 6. Write a function `copy_file_content` that takes two filenames (source and destination),
# and copies the content of the source file to the destination file.
# Example:
# Input: copy_file_content('source.txt', 'destination.txt')
# (Content of 'source.txt' -> 'This is the source file.')
# (Content of 'destination.txt' -> 'This is the source file.')

def copy_file_content(filname1 , filename2):
    file1 = open(filname1 , 'r')
    file2 = open(filename2, 'a')

    for lines in file1:
        file2.write(lines)
    
    file1.close()
    file2.close()

Input = copy_file_content('lines1.txt', 'lines3.txt')
print("succesfull")

