# Assignment: Lists, Dictionaries, Nested Lists and Dictionaries, and Functions

# 1. Write a function `create_student` that takes a student's name and a list of subjects,
# and returns a dictionary representing the student with their name and an empty list of grades for each subject.
# Example:
# Input: create_student("Alice", ["Math", "Science"])
# Output: {'name': 'Alice', 'grades': {'Math': [], 'Science': []}}

# 2. Write a function `add_grade` that takes a student dictionary, a subject, and a grade,
# and adds the grade to the list of grades for that subject.
# Example:
# Input: student = {'name': 'Alice', 'grades': {'Math': [], 'Science': []}}
#        add_grade(student, 'Math', 90)
# Output: {'name': 'Alice', 'grades': {'Math': [90], 'Science': []}}

# 3. Write a function `calculate_average` that takes a list of grades and returns the average grade.
# Example:
# Input: calculate_average([90, 80, 70])
# Output: 80.0

# 4. Write a function `student_average` that takes a student dictionary and a subject,
# and returns the average grade for that subject.
# Example:
# Input: student = {'name': 'Alice', 'grades': {'Math': [90, 80, 70], 'Science': [100, 90]}}
#        student_average(student, 'Math')
# Output: 80.0

# 5. Write a function `overall_average` that takes a student dictionary and returns the student's overall average grade.
# Example:
# Input: student = {'name': 'Alice', 'grades': {'Math': [90, 80, 70], 'Science': [100, 90]}}
#        overall_average(student)
# Output: 86.01

# 6. Write a function `create_class` that takes a class name and a list of students (each represented by a dictionary),
# and returns a dictionary representing the class.
# Example:
# Input: student1 = {'name': 'Alice', 'grades': {'Math': [90, 80, 70], 'Science': [100, 90]}}
#        student2 = {'name': 'Bob', 'grades': {'Math': [70, 80], 'Science': [90, 100]}}
#        create_class("MathClass", [student1, student2])
# Output: {'class_name': 'MathClass', 'students': [student1, student2]}

# 7. Write a function `class_average` that takes a class dictionary and a subject,
# and returns the average grade for that subject across all students.
# Example:
# Input: class_ = {'class_name': 'MathClass', 'students': [student1, student2]}
#        class_average(class_, 'Math')
# Output: 80.0

# 8. Write a function `overall_class_average` that takes a class dictionary and returns the overall average grade for
# the class. Example: Input: class_ = {'class_name': 'MathClass', 'students': [student1, student2]}
# overall_class_average(class_) Output: 85.0

# 9. Write a function `add_student_to_class` that takes a class dictionary and a student dictionary,
# and adds the student to the class.
# Example:
# Input: class_ = {'class_name': 'MathClass', 'students': [student1]}
#        add_student_to_class(class_, student2)
# Output: {'class_name': 'MathClass', 'students': [student1, student2]}

# 10. Write a function `remove_student_from_class` that takes a class dictionary and a student's name,
# and removes the student from the class.
# Example:
# Input: class_ = {'class_name': 'MathClass', 'students': [student1, student2]}
#        remove_student_from_class(class_, 'Bob')
# Output: {'class_name': 'MathClass', 'students': [student1]}
