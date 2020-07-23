import sqlite3
from tkinter import *

def mySave():
    conn = sqlite3.connect("C:\\sqlite\\test.db")
    print("Opened database successfully")

    sql = "INSERT INTO COMPANY2 VALUES ({},\'{}\',{},\'{}\',{})"\
        .format(id.get(), name.get(), age.get(), address.get(), salary.get())
    # print(sql)

    conn.execute(sql)
    conn.commit()
    conn.close()
    print("Done")

master = Tk()

id = IntVar()
name = StringVar()
age = IntVar()
address = StringVar()
salary = StringVar()

lbl_id = Entry(master, textvariable=id).grid(row=0, column=0)
lbl_name = Entry(master, textvariable=name).grid(row=1, column=0)
lbl_age = Entry(master, textvariable=age).grid(row=2, column=0)
lbl_address = Entry(master, textvariable=address).grid(row=3, column=0)
lbl_salary = Entry(master, textvariable=salary).grid(row=4, column=0)
btn_save = Button(master, text = "Save", command=mySave).grid(row=5, column=0)

master.mainloop()