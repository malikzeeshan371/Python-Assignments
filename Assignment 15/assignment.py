# Assignment: Basics of File Handling in Python

# 1. Write a function `write_message_to_file` that takes a filename and a string message,
# and writes the message to the file. If the file already exists, it should overwrite the content.
# Example:
# Input: write_message_to_file('message.txt', 'Hello, World!')
# (Content of 'message.txt' -> 'Hello, World!')

# 2. Write a function `read_message_from_file` that takes a filename,
# and returns the content of the file as a string.
# Example:
# Input: read_message_from_file('message.txt')
# Output: 'Hello, World!'

# 3. Write a function `append_message_to_file` that takes a filename and a string message,
# and appends the message to the file.
# Example:
# Input: append_message_to_file('message.txt', ' Goodbye!')
# (Content of 'message.txt' -> 'Hello, World! Goodbye!')

# 4. Write a function `write_lines_to_file` that takes a filename and a list of strings,
# and writes each string to a new line in the file.
# Example:
# Input: write_lines_to_file('lines.txt', ['Line 1', 'Line 2', 'Line 3'])
# (Content of 'lines.txt' -> 'Line 1\nLine 2\nLine 3\n')

# 5. Write a function `read_lines_from_file` that takes a filename,
# and returns a list of strings, where each string is a line from the file.
# Example:
# Input: read_lines_from_file('lines.txt')
# Output: ['Line 1', 'Line 2', 'Line 3']

# 6. Write a function `copy_file_content` that takes two filenames (source and destination),
# and copies the content of the source file to the destination file.
# Example:
# Input: copy_file_content('source.txt', 'destination.txt')
# (Content of 'source.txt' -> 'This is the source file.')
# (Content of 'destination.txt' -> 'This is the source file.')

# 7. Write a function `count_words_in_file` that takes a filename,
# and returns the number of words in the file.
# Example:
# Input: count_words_in_file('words.txt')
# (Content of 'words.txt' -> 'This is a file with some words.')
# Output: 7

# 8. Write a function `find_and_replace_in_file` that takes a filename, a target string, and a replacement string,
# and replaces all occurrences of the target string with the replacement string in the file.
# Example:
# Input: find_and_replace_in_file('example.txt', 'old', 'new')
# (Content of 'example.txt' before -> 'This old house.')
# (Content of 'example.txt' after -> 'This new house.')

# 9. Write a function `remove_empty_lines` that takes a filename,
# and removes all empty lines from the file.
# Example:
# Input: remove_empty_lines('lines.txt')
# (Content of 'lines.txt' before -> 'Line 1\n\nLine 2\n\nLine 3\n')
# (Content of 'lines.txt' after -> 'Line 1\nLine 2\nLine 3\n')

# 10. Write a function `file_statistics` that takes a filename,
# and returns a dictionary with the number of characters, words, and lines in the file.
# Example:
# Input: file_statistics('example.txt')
# (Content of 'example.txt' -> 'This is a file.\nIt has multiple lines.\nAnd some words.')
# Output: {'characters': 49, 'words': 10, 'lines': 3}
