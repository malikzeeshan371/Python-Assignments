# 9. Write a function `search_in_file` that takes a filename and a search term,
# and prints all lines that contain the search term, with the line numbers.
# Example:
# Input: search_in_file('example.txt', 'search')
# (Content of 'example.txt' -> 'Line 1\nThis line contains search term.\nAnother search line.\n')
# Output:
# Line 2: This line contains search term.
# Line 3: Another search line.

def search_in_file(filename, searchterm):
    with open(filename , 'r') as file:
        lines = file.readlines()
        file.close()
    
        for number,line in enumerate(lines , 1):
          if searchterm in line:
            print(f"Line {number} : {line}")


search_in_file('Assignment 17/searchterm9.txt', 'search')
