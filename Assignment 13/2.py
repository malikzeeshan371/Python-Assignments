
# 2. Write a function `add_grade` that takes a student dictionary, a subject, and a grade,
# and adds the grade to the list of grades for that subject.
# Example:
# Input: student = {'name': 'Alice', 'grades': {'Math': [], 'Science': []}}
#        add_grade(student, 'Math', 90)
# Output: {'name': 'Alice', 'grades': {'Math': [90], 'Science': []}}




def add_grade(student , subject , grade):
    if subject in student['grades']:
        student['grades'][subject].append(grade)
  

    return student
    
student =  {'name': 'Alice', 'grades': {'Math': [], 'Science': []}}
output = add_grade(student , 'Math' , 90)
print(output)
print("\n")

    