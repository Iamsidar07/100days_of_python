import random

# List Comprehension

# new_list = [new_item for item in list]

numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
# print(new_list)

# List Comprehension

# new_list = [new_item for item in list]
# Conditional List Comprehension
# new_list = [new_item for item in list if condition]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
long_names = [name.upper() for name in names if len(name) >= 5]

# Dictionary Comprehension
# new_dict = {new_key:new_value for value in list}
# new_dict = {new_key:new_value for (key,value) in dict.items() if condition}

student_scores = {name: random.randint(1, 100) for name in names}
print(student_scores)

passed_students = {name: score for (name, score) in student_scores.items() if score >= 60}
print(passed_students)
