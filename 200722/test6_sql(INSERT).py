import sqlite3
import sys

conn = sqlite3.Connection("C:\\sqlite\\test.db")
print("conn ok")

sys.stdin = open("userlist.txt", 'r', encoding="UTF-8")

for inp in sys.stdin.readlines():
    sql = "INSERT INTO COMPANY2 VALUES ({})".format(inp)
    conn.execute(sql)

conn.commit()
print("Success")
conn.close()