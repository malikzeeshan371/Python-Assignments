# 9. Create a nested dictionary representing a directory structure, then print all file paths. Example: {'root': {
# 'folder1': {'file1.txt': 'content1'}, 'folder2': {'file2.txt': 'content2'}}} should print /root/folder1/file1.txt
# and /root/folder2/file2.txt
directory = {
    'root': {
        'folder1': {
            'file1.txt': 'content1',
            
            }, 
        'folder2': {
            'file2.txt': 'content2',
            }
        }
    } 

path = "/root"

for folder,files in directory['root'].items():
    for file in files:
        print(f"{path}/{folder}/{file}")