# 5. Write a function `overall_average` that takes a student dictionary and returns the student's overall average grade.
# Example:
# Input: student = {'name': 'Alice', 'grades': {'Math': [90, 80, 70], 'Science': [100, 90]}}
#        overall_average(student)
# Output: 86.01
def overall_average(student):
    total_sum = 0
    total_count = 0
    for grades in student['grades'].values():
       
         total_sum = total_sum + sum(grades)
         total_count = total_count + len(grades)

    return total_sum/total_count
   
        
student = {'name': 'Alice', 
           'grades': {'Math': [90, 80, 70],
                       'Science': [100, 90]}}

average = overall_average(student)
print( "Overall average is : " , average)
print("\n")
