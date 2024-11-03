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
