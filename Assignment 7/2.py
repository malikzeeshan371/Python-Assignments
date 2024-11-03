 
# 3. Add a new subject and score for an existing student. Example: {'Alice': {'Math': 90, 'Science': 85}} should add
# English with score 88 for Alice, resulting in {'Alice': {'Math': 90, 'Science': 85, 'English': 88}}
dict_score = {'Alice':{'Maths':90, 'Science': 85}, 'Bob':{'Maths': 78, 'Science':82}}
new_subject = {'English':82}
dict_score['Alice'].update(new_subject)
print(dict_score['Alice'])
print('\n')