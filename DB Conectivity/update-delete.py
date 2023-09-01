import sqlite3

connection = sqlite3.connect('univ.db')
cursor = connection.cursor()
cursor.execute("update Dept set name='Engineering' where name = 'Eng'")
cursor.execute("delete from Dept where deptNo = 40")
connection.commit()
cursor.close()
