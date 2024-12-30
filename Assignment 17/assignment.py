# Assignment: Advanced File Handling in Python

# 1. Write a function `read_file_in_chunks` that takes a filename and a chunk size,
# and reads the file in chunks of the given size. Print each chunk.
# Example:
# Input: read_file_in_chunks('example.txt', 10)
# Output:
# Chunk 1: 'This is th'
# Chunk 2: 'e content '
# (Continue until the end of the file)

# 2. Write a function `write_list_of_dicts_to_file` that takes a filename and a list of dictionaries,
# and writes each dictionary to a new line in the file in JSON format.
# Example:
# Input: write_list_of_dicts_to_file('data.txt', [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}])
# (Content of 'data.txt' -> '{"name": "Alice", "age": 25}\n{"name": "Bob", "age": 30}\n')

# 3. Write a function `read_file_into_dict` that takes a filename where each line is a JSON string of a dictionary,
# and returns a list of dictionaries.
# Example:
# Input: read_file_into_dict('data.txt')
# (Content of 'data.txt' -> '{"name": "Alice", "age": 25}\n{"name": "Bob", "age": 30}\n')
# Output: [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]

# 4. Write a function `merge_files` that takes two filenames (file1 and file2),
# and writes the content of both files into a new file with lines from file1 and file2 interleaved.
# Example:
# Input: merge_files('file1.txt', 'file2.txt', 'merged.txt')
# (Content of 'file1.txt' -> 'Line 1 from file1\nLine 2 from file1\n')
# (Content of 'file2.txt' -> 'Line 1 from file2\nLine 2 from file2\n')
# (Content of 'merged.txt' -> 'Line 1 from file1\nLine 1 from file2\nLine 2 from file1\nLine 2 from file2\n')

# 5. Write a function `reverse_file_content` that takes a filename,
# and writes the content of the file in reverse order to a new file.
# Example:
# Input: reverse_file_content('example.txt', 'reversed.txt')
# (Content of 'example.txt' -> 'Line 1\nLine 2\nLine 3\n')
# (Content of 'reversed.txt' -> 'Line 3\nLine 2\nLine 1\n')

# 6. Write a function `filter_file_by_word` that takes a filename and a word,
# and writes only the lines that contain the word to a new file.
# Example:
# Input: filter_file_by_word('example.txt', 'keyword', 'filtered.txt')
# (Content of 'example.txt' -> 'This is a line with keyword.\nThis is a line without.\nAnother line with keyword.\n')
# (Content of 'filtered.txt' -> 'This is a line with keyword.\nAnother line with keyword.\n')

# 7. Write a function `count_word_occurrences` that takes a filename and a word,
# and returns the number of occurrences of the word in the file.
# Example:
# Input: count_word_occurrences('example.txt', 'word')
# (Content of 'example.txt' -> 'word1 word2 word word3 word word')
# Output: 3

# 8. Write a function `split_file` that takes a filename and a line count,
# and splits the file into multiple smaller files, each containing the given number of lines.
# Example:
# Input: split_file('example.txt', 2)
# (Content of 'example.txt' -> 'Line 1\nLine 2\nLine 3\nLine 4\nLine 5\n')
# Output:
# (Content of 'example_part1.txt' -> 'Line 1\nLine 2\n')
# (Content of 'example_part2.txt' -> 'Line 3\nLine 4\n')
# (Content of 'example_part3.txt' -> 'Line 5\n')

# 9. Write a function `search_in_file` that takes a filename and a search term,
# and prints all lines that contain the search term, with the line numbers.
# Example:
# Input: search_in_file('example.txt', 'search')
# (Content of 'example.txt' -> 'Line 1\nThis line contains search term.\nAnother search line.\n')
# Output:
# Line 2: This line contains search term.
# Line 3: Another search line.

# 10. Write a function `create_backup` that takes a filename,
# and creates a backup of the file with a '.bak' extension.
# Example:
# Input: create_backup('example.txt')
# (Content of 'example.txt' -> 'Backup this file.')
# (Creates 'example.txt.bak' with the same content)
