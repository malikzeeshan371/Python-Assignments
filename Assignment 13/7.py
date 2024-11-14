# 7. Write a function `class_average` that takes a class dictionary and a subject,
# and returns the average grade for that subject across all students.
# Example:
# Input: class_ = {'class_name': 'MathClass', 'students': [student1, student2]}
#        class_average(class_, 'Math')
# Output: 80.0
def class_average(class_ , subject ):
    total_sum = 0
    total_count = 0
    for student in class_['students']:
        grades = student['grades'][subject]

        for grade in grades:
            total_sum += grade
            total_count += 1

    return total_sum/total_count
    
    
student1 = {'name': 'Alice', 'grades': {'Math': [90, 80, 70], 'Science': [100, 90]}}
student2 = {'name': 'Alice', 'grades': {'Math': [90, 80, 70], 'Science': [100, 90]}}   
class_ =  {'class_name': 'MathClass', 'students': [student1, student2]}
print("The average of Math subject is: " , class_average(class_ , 'Math'))
print("\n")
