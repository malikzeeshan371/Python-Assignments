# 5. Calculate the average score of each student and add it to their dictionary. Example: [{'name': 'Alice',
# 'scores':
# {'Math': 90, 'Science': 85}}, {'name': 'Bob', 'scores': {'Math': 78, 'Science': 82}}] should add average
# scores resulting in [{'name': 'Alice', 'scores': {'Math': 90, 'Science': 85}, 'average': 87.5}, {'name': 'Bob',
# 'scores': {'Math': 78, 'Science': 82}, 'average': 80.0}]
students = [{'Name':'Alice','Scores':{'Maths':90 , 'Science':85, }},{'Name':'Bob', 'Scores':{'Maths':78,
                                                                                               'Science':82}}]

for student in students:
    scores = student['Scores'].values()
    average = sum(scores)/len(scores)
    student['Average'] = average
print(students)
print('\n')
