import Student
import pickle

students = [Student.Student(10, 'Juan', 'CS'), Student.Student(11, 'Juana', 'HR'), Student.Student(12, 'Sofía', 'TI'), ]
with open('students.data', 'wb') as file:
    for student in students:
        pickle.dump(student, file)
