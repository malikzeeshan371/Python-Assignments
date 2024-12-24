# 1. Write a function `write_message_to_file` that takes a filename and a string message,
# and writes the message to the file. If the file already exists, it should overwrite the content.
# Example:
# Input: write_message_to_file('message.txt', 'Hello, World!')
# (Content of 'message.txt' -> 'Hello, World!')

def write_message_to_file(filename , message):

        with open (filename , 'w') as f:
            f.write(message)
            print('File' , filename , 'created successfully')

    


input = write_message_to_file('Assignment 15/message.txt' , 'Hello World')
print(input)
