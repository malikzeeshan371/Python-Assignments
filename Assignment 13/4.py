
# 4. Write a function `student_average` that takes a student dictionary and a subject,
# and returns the average grade for that subject.
# Example:
# Input: student = {'name': 'Alice', 'grades': {'Math': [90, 80, 70], 'Science': [100, 90]}}
#        student_average(student, 'Math')
# Output: 80.0
def student_average(student , subject):
    total_sum = 0
    #total_count = 0
    grades = student['grades'][subject]
    for grade in grades:
            total_sum += grade
            
    
    return total_sum/len(grades)
        
    


student = {'name': 'Alice', 'grades': {'Math': [90, 80,70], 'Science': [100,90]}}
average = student_average(student , 'Math')
print( "Average of subject Math is : " , average)
print("\n")

