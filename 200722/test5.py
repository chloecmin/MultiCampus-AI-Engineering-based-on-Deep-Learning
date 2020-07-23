import sqlite3
conn = sqlite3.Connection("C:\\sqlite\\test.db")
print("conn ok")

sql = '''CREATE TABLE COMPANY2
        (ID INT PARIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,
        AGE INT NOT NULL,
        ADDRESS CHAR(50),
        SALARY REAL);'''

conn.execute(sql)
conn.close()

print("Success")