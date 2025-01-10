
# 1. Write a function `read_file_in_chunks` that takes a filename and a chunk size,
# and reads the file in chunks of the given size. Print each chunk.
# Example:
# Input: read_file_in_chunks(   'example.txt', 10)
# Output:
# Chunk 1: 'This is th'
# Chunk 2: 'e content '
# (Continue until the end of the file)

def read_file_in_chunks(filename,chunk_size):
    with open(filename, 'r') as file:
        chunk_number = 1

        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            print(f"Chunk {chunk_number} : '{chunk}'")
            chunk_number += 1
    file.close()

    
       
        


read_file_in_chunks('Assignment 17/example.txt' , 10) 
