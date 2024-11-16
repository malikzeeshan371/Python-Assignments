
# 8. Write a function `overall_class_average` that takes a class dictionary and returns the overall average grade for
# the class. Example: 
# Input: class_ = {'class_name': 'MathClass', 'students': [student1, student2]}
# overall_class_average(class_)
#  Output: 85.0
def overall_class_average(class_):
    total_sum =0
    total_count = 0
    for student in class_['students']:
        for grades in student['grades'].values():
            for grade in grades:
               total_sum += grade
               total_count += 1
    return total_sum/total_count


student1 = {'name': 'Alice', 'grades': {'Math': [90, 80, 70], 'Science': [100, 90]}}
student2 = {'name': 'Bob', 'grades': {'Math': [90, 80, 70], 'Science': [100, 90]}} 
class_ =  {'class_name': 'MathClass', 'students': [student1, student2]}
print(overall_class_average(class_))