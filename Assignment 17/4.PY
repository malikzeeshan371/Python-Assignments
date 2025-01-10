
# 4. Write a function `merge_files` that takes two filenames (file1 and file2),
# and writes the content of both files into a new file with lines from file1 and file2 interleaved.
# Example:
# Input: merge_files('file1.txt', 'file2.txt', 'merged.txt')
# (Content of 'file1.txt' -> 'Line 1 from file1\nLine 2 from file1\n')
# (Content of 'file2.txt' -> 'Line 1 from file2\nLine 2 from file2\n')
# (Content of 'merged.txt' -> 'Line 1 from file1\nLine 1 from file2\nLine 2 from file1\nLine 2 from file2\n')

def merge_files(file1, file2, merged_file):
    # filenames = [file1 , file2]
    # with open(file3 , 'w') as outfile:

    #     for names in filenames:
    #         with open(names) as innerfile:
    #             outfile.write(innerfile.read())

    #         outfile.write('\n')
    # return 'success'

    with open(file1, 'r') as f1, open(file2, 'r') as f2 , open(merged_file , 'w') as mf:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        # f1.close()
        # f2.close()

        max_len = max(len(lines1) , len(lines2))

        for i in range(max_len):
            if i < len(lines1):
                mf.write(lines1[i])
            if i < len(lines2):
                mf.write(lines2[i])

    return 'success'  
    


print(merge_files('Assignment 17/file1.txt', 'Assignment 17/file2.txt', 'Assignment 17/merged.txt'))



