
# 8. Write a function `split_file` that takes a filename and a line count,
# and splits the file into multiple smaller files, each containing the given number of lines.
# Example:
# Input: split_file('example.txt', 2)
# (Content of 'example.txt' -> 'Line 1\nLine 2\nLine 3\nLine 4\nLine 5\n')
# Output:
# (Content of 'example_part1.txt' -> 'Line 1\nLine 2\n')
# (Content of 'example_part2.txt' -> 'Line 3\nLine 4\n')
# (Content of 'example_part3.txt' -> 'Line 5\n')

def split_file(filename,line_count):
    with open(filename , 'r') as file:
        lines = file.readlines()
        print(lines)

    total_lines = len(lines)
    print(total_lines)
    total_parts = (total_lines + line_count -1)// line_count
    print(total_parts)

    for i in range(total_parts):
        part_of_filename = f"{filename}_part{i+1}.txt"
        with open(part_of_filename, 'w') as part_file:
            part_file.writelines(lines[i * line_count:(i+1) * line_count])
        print(f"created {part_of_filename}")

        
split_file('Assignment 17/example8.txt' , 2)
    