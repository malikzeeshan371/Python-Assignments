# 1. Write a function `create_student` that takes a student's name and a list of subjects,
# and returns a dictionary representing the student with their name and an empty list of grades for each subject.
# Example:
# Input: create_student("Alice", ["Math", "Science"])
# Output: {'name': 'Alice', 'grades': {'Math': [], 'Science': []}}

def create_student(name , subjects):
    return {
        'name' : name,
        'grades': {subject : [] for subject in subjects}
    }
student = create_student('Alice' ,['Math' , 'Science'] )
print(student)
print("\n")

