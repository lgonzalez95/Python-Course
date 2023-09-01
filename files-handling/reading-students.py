import Student, pickle

with open('students.data', 'rb') as file:
    for i in range(2):
        s = pickle.load(file)
        s.display()
