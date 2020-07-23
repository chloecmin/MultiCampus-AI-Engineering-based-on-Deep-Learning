import sqlite3

conn = sqlite3.connect("C:\\sqlite\\test.db")
print("Opened database successfully")

cursor = conn.execute("SELECT id, name, address, salary from COMPANY2")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("ADDRESS = ", row[2])
    print("SALARY = ", row[3])
    print("Operation done successfully", "\n")

conn.close()