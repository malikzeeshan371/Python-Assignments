
# 10. Write a function `create_backup` that takes a filename,
# and creates a backup of the file with a '.bak' extension.
# Example:
# Input: create_backup('example.txt')
# (Content of 'example.txt' -> 'Backup this file.')
# (Creates 'example.txt.bak' with the same content)

import shutil
def create_backup(filename):
    backup_filename = f"{filename}.bak"

    shutil.copy(filename , backup_filename)
    print(f"Backup created: {backup_filename}")



create_backup('Assignment 17/backup10.txt')




