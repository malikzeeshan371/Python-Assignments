# 9. Write a function `add_student_to_class` that takes a class dictionary and a student dictionary,
# and adds the student to the class.
# Example:
# Input: class_ = {'class_name': 'MathClass', 'students': [student1]}
#        add_student_to_class(class_, student2)
# Output: {'class_name': 'MathClass', 'students': [student1, student2]}
def add_student_to_class(class_ , student):
    class_.update(student)
    return{
        'classname' : class_,
        'students' : [student]
    }

student1 = {'name': 'Alice', 'grades': {'Math': [90, 80, 70], 'Science': [100, 90]}}
student2 = {'name': 'Alice', 'grades': {'Math': [90, 80, 70], 'Science': [100, 90]}}   

class_ = {'class_name': 'MathClass', 'students': [student1]}
print(add_student_to_class(class_, student2))