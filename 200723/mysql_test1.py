# mysql connection

import mysql.connector

conn = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='employees')
cursor = conn.cursor()
cursor.execute("SELECT DATABASE()")
data = cursor.fetchone()
print("Connection established to: ",data)

conn.close()

# Search Table
import mysql.connector

conn = mysql.connector.connect(
   user='root', password='1234', host='127.0.0.1', database='employees')

cursor = conn.cursor()

sql = "SELECT * from employees.employees"

cursor.execute(sql)

result = cursor.fetchone();
print(result)

result = cursor.fetchall();
print(result)

conn.close()

# insert table

import mysql.connector

conn = mysql.connector.connect(
   user='root', password='1234', host='127.0.0.1', database='company')

cursor = conn.cursor()

sql = "INSERT INTO company.emp VALUES (2, '세종대왕')"

try:
   cursor.execute(sql)
   conn.commit()
   print("insert ok")

except:
   conn.rollback()

conn.close()