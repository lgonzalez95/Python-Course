import sqlite3

connection = sqlite3.connect('univ.db')
cursor = connection.cursor()
cursor.execute('create table Student(rollNum integer primary key , name text, city tex, deptNo integer, foreign key (deptNo) references  Dept(deptNo))')

cursor.execute("insert into Dept values (10, 'CSE')")
cursor.execute("insert into Dept values (20, 'ECE')")
cursor.execute("insert into Dept values (30, 'Civil')")
cursor.execute("insert into Dept values (40, 'Eng')")
cursor.execute("insert into Dept values (50, 'Mech')")

data = [
    ['Ajay', 'Delhi', 10],
    ['Vijay', 'Kolkata', 10],
    ['Ajay', 'Mumbai', 20],
    ['Ramesh', 'Delhi', 30],
    ['Suneeta', 'Lucknow', 40],
    ['Anita', 'Kolkata', 30],
    ['Raj', 'Jaipur', 30],
    ['Ali', 'Lucknow', 40],
    ['Michael', 'Cochin', 10],
    ['Pavan', 'Vijaywada', 20],
    ['Suraj', 'Hyderabad', 10],
    ['Altaf', 'Bangaluru', 40],
    ['Ravi', 'Indore', 20],
    ['Verma', 'Delhi', 20],
    ['Sharma', 'Vizag', 10],

]

for x in range(0, 15):
    cursor.execute(f"insert into Student values({x}+1, '{data[x][0]}', '{data[x][1]}','{data[x][2]}')")

connection.commit()
cursor.close()
