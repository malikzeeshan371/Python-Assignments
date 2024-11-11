# 6. Write a function `create_class` that takes a class name and a list of students (each represented by a dictionary),
# and returns a dictionary representing the class.
# Example:
# Input: student1 = {'name': 'Alice', 'grades': {'Math': [90, 80, 70], 'Science': [100, 90]}}
#        student1 = {'name': 'Alice', 'grades': {'Math': [90, 80, 70], 'Science': [100, 90]}}
#        create_class("MathClass", [student1, student2])
# Output: {'class_name': 'MathClass', 'students': [student1, student2]}
def create_class(classname , students ):
    return{
        'classname' : classname,
        'students' : students
    }
student1 = {'name': 'Alice', 'grades': {'Math': [90, 80, 70], 'Science': [100, 90]}}
student2 = {'name': 'Alice', 'grades': {'Math': [90, 80, 70], 'Science': [100, 90]}}
class_info = create_class('MathClass' , [student1 ,student2] )
print(class_info)
print("\n")
