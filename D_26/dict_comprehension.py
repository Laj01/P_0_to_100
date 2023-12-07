import random


students = ['Paola Porter', 'Rhett Gutierrez', 'Savannah Randolph', 'Eugene Esquivel', 'Jaylee Villegas', 'Clyde Bell']

student_scores = {student:random.randint(1, 100) for student in students}

students_passed = {student:score for (student, score) in student_scores.items() if score > 60}



print(students_passed)