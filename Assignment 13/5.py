# 5. Write a function `overall_average` that takes a student dictionary and returns the student's overall average grade.
# Example:
# Input: student = {'name': 'Alice', 'grades': {'Math': [90, 80, 70], 'Science': [100, 90]}}
#        overall_average(student)
# Output: 86.01
def overall_average(student):
    total_sum = 0
    total_count = 0
    
    
    for subject,grades in student['grades'].items():
     for grade in grades:

     
       
      total_sum += grade
      total_count += 1
         

    return total_sum/total_count
   
        
student = {'name': 'Alice', 
           'grades': {'Math': [90, 80, 70],
                       'Science': [100, 90]}}

average = overall_average(student)
print( "Overall average is : " , average)
print("\n")
