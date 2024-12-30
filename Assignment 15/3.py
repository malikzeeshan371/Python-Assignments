
# 3. Write a function `append_message_to_file` that takes a filename and a string message,
# and appends the message to the file.
# Example:
# Input: append_message_to_file('message.txt', ' Goodbye!')
# (Content of 'message.txt' -> 'Hello, World! Goodbye!')

def append_message_to_file(filename , message):
    with open(filename , 'a') as file:
        file.write(message)
        file.close()

    print ('this is to append the' , filename , 'with new message')



append_message_to_file('Assignment 15/message.txt', ' Goodbye!')

