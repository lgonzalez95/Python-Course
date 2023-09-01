import sqlite3

connection = sqlite3.connect('univ.db')
cursor = connection.cursor()

rows = cursor.execute("select * from Student")
print(rows.fetchone())
print(rows.fetchmany(3))
print(rows.fetchall())

dept_names = cursor.execute("select name from Dept")
for t in dept_names:
    print('Dept Name:', t[0])


student_names = cursor.execute("select distinct(name) from Student where name like 'A%'")
print(student_names.fetchall())

joined_data = cursor.execute("""
                            select s.name, s.city, d.name
                            from Student s 
                            inner join Dept d 
                            ON s.deptNo = d.deptNo""")
for s in joined_data:
    print(s)
cursor.close()
