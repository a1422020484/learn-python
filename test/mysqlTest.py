import mysql.connector

conn = mysql.connector.connect(user='root', password='root', database='mybatisplus')
cursor = conn.cursor()
cursor.execute("create table user_python (id varchar(20) primary key, name varchar(20))")

cursor.execute('insert into user_python (id, name) values (%s, %s)', ['1', 'Michael'])

print(cursor.rowcount)

conn.commit()

cursor.execute('select * from user_python where id = %s', ('1',))

values = cursor.fetchall()

print(values)

cursor.close()

conn.close()
