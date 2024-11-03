# Advanced Assignment: Working with Nested Dictionaries and Lists
# 1. Create a dictionary with student names as keys and their subjects with scores as values.
# Example: {'Alice': {'Math': 90, 'Science': 85}, 'Bob': {'Math': 78, 'Science': 82}}
dict_score = {'Alice': {'Maths': 90, 'Science': 85}, 'Bob': {'Maths': 78, 'Science': 82}}
print(dict_score)
print('\n')

# 2. Print the score of a specific student in a specific subject. Example: For {'Alice': {'Math': 90, 'Science': 85},
# 'Bob': {'Math': 78, 'Science': 82}}, print the Science score for Alice, which is 85
dict_score = {'Alice': {'Maths': 90, 'Science': 85}, 'Bob': {'Maths': 78, 'Science': 82}}
print(dict_score['Alice']['Science'])
print('\n')

# 3. Add a new subject and score for an existing student. Example: {'Alice': {'Math': 90, 'Science': 85}} should add
# English with score 88 for Alice, resulting in {'Alice': {'Math': 90, 'Science': 85, 'English': 88}}
dict_score = {'Alice': {'Maths': 90, 'Science': 85}, 'Bob': {'Maths': 78, 'Science': 82}}
new_subject = {'English': 82}
dict_score['Alice'].update(new_subject)
print(dict_score['Alice'])
print('\n')

# 4. Create a list of dictionaries, each representing a student with their subjects and scores. Example: [{'name':
# 'Alice', 'scores': {'Math': 90, 'Science': 85}}, {'name': 'Bob', 'scores': {'Math': 78, 'Science': 82}}]
list_dict2 = [{'Name': 'Alice', 'Scores': {'Maths': 90, 'Science': 85, }}, {'Name': 'Bob', 'Scores': {'Maths': 78,
                                                                                                      'Science': 82}}]
print(list_dict2)
print('\n')

# 5. Calculate the average score of each student and add it to their dictionary. Example: [{'name': 'Alice',
# 'scores':
# {'Math': 90, 'Science': 85}}, {'name': 'Bob', 'scores': {'Math': 78, 'Science': 82}}] should add average
# scores resulting in [{'name': 'Alice', 'scores': {'Math': 90, 'Science': 85}, 'average': 87.5}, {'name': 'Bob',
# 'scores': {'Math': 78, 'Science': 82}, 'average': 80.0}]
students = [{'Name': 'Alice', 'Scores': {'Maths': 90, 'Science': 85, }}, {'Name': 'Bob', 'Scores': {'Maths': 78,
                                                                                                    'Science': 82}}]

for student in students:
    scores = student['Scores'].values()
    average = sum(scores) / len(scores)
    student['Average'] = average
print(students)
print('\n')

# 6. Find and print the student with the highest average score. Example: [{'name': 'Alice', 'scores': {'Math': 90,
# 'Science': 85}, 'average': 87.5}, {'name': 'Bob', 'scores': {'Math': 78, 'Science': 82}, 'average': 80.0}] should
# print "Alice"
students = [{'Name': 'Alice', 'Scores': {'Maths': 90, 'Science': 85}, 'Average': 87.5},
            {'Name': 'Bob', 'Scores': {'Maths': 78, 'Science': 82}, 'Average': 80.0}]
highest_avg_student = students[0]
highest_avg = students[0]['Average']

for student in students:
    if student['Average'] > highest_avg:
        highest_avg = student['Average']
        highest_avg_student = student
print(highest_avg_student['Name'])
print('\n')

# 7. Create a nested dictionary from a list of tuples. Example: tuples = [('Alice', 'Math', 90), ('Alice', 'Science',
# 85), ('Bob', 'Math', 78), ('Bob', 'Science', 82)] should create {'Alice': {'Math': 90, 'Science': 85},
# 'Bob': {'Math': 78, 'Science': 82}}
tups = [('Alice', 'Math', 90), ('Alice', 'Science', 85), ('Bob', 'Math', 78), ('Bob', 'Science', 82)]
nested_dict = {}
for name, subject, score in tups:
    if name not in nested_dict:
        nested_dict[name] = {}
    nested_dict[name][subject] = score
print(nested_dict)
print('\n')

# 8. Create a dictionary where the keys are student names and the values are lists of their scores.
# Example: {'Alice': [90, 85], 'Bob': [78, 82]}
student_scores = {}
student_scores["Alice"] = [85, 90]
student_scores["Bob"] = [78, 82]
print(student_scores)
print('\n')

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

for folder, files in directory['root'].items():
    for file in files:
        print(f"{path}/{folder}/{file}")
