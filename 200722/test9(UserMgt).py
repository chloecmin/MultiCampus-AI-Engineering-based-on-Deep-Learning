import sqlite3
from tkinter import *
from tkinter import messagebox

def addUser():
    try:
        conn = sqlite3.connect("C:\\sqlite\\test2.db")
        print("Opened database successfully")

        sql = "INSERT INTO USER VALUES ({},\'{}\')".format(id.get(), name.get())

        conn.execute(sql)
        conn.commit()
        messagebox.showinfo("", "추가되었습니다.")
    except Exception as e:
        print(e)
    finally:
        conn.close()
        selectUser()
def updateUser():
    try :
        conn = sqlite3.connect("C:\\sqlite\\test2.db")
        print("Opened database successfully")

        sql = "UPDATE USER SET NAME=\'{}\' WHERE ID={}".format(name.get(), id.get())

        conn.execute(sql)
        conn.commit()
        messagebox.showinfo("", "수정되었습니다.")
    except Exception as e:
        print(e)
    finally:
        conn.close()
        selectUser()
def deleteUser():
    try :
        if id.get() == "":
            messagebox.showinfo("","삭제할 ID를 입력하세요.")
        elif name.get() == "":
            messagebox.showinfo("","삭제할 이름을 입력하세요")
        else:
            conn = sqlite3.connect("C:\\sqlite\\test2.db")
            print("Opened database successfully")

            sql = "DELETE FROM USER WHERE (NAME=\'{}\' and ID={})".format(name.get(), id.get())

            conn.execute(sql)
            conn.commit()
            messagebox.showinfo("", "삭제되었습니다.")
    except Exception as e:
        print(e)
    finally:
        conn.close()
        selectUser()
def selectUser():
    try:
        conn = sqlite3.connect("C:\\sqlite\\test2.db")
        print("Opened database successfully")

        sql = "SELECT * FROM USER"
        cursor = conn.execute(sql)

        users = cursor.fetchall()
        for user in users:
            pass

        #그리드 자체를 초기화하는 방법
        for i in bottom.grid_slaves():
            i.grid_forget()

        height = len(users)
        width = len(users[0])
        for i in range(height):
            for j in range(width):
                listentry = Entry(bottom)
                listentry.insert(0, users[i][j])
                listentry.grid(row=i, column=j)
    except Exception as e:
        print(e)
    finally:
        conn.close()
def searchUser():
    try:
        master2 = Tk()
        strData = []

        master2.title("DB 목록 보기")
        master2.geometry("200x170")

        list_id = Listbox(master2, width=5)
        list_name = Listbox(master2)
        list_id.pack(side=LEFT, expand=1)
        list_name.pack(side=LEFT, expand=1)

        conn = sqlite3.connect("C:\\sqlite\\test2.db")
        print("Opened database successfully")

        sql = "SELECT * FROM USER"
        cursor = conn.execute(sql)

        """서치하는 방법1"""
        # for row in cursor:
        #     strData.append([row[0],row[1]])

        """서치하는 방법2"""
        # users = cursor.fetchall()
        # for user in users:
        #     strData.append(user)

        """서치하는 방법3"""
        while(1):
            users = cursor.fetchone()
            if users == None: break
            strData.append(users)

        for data in strData:
            list_id.insert(END, data[0])
            list_name.insert(END, data[1])
    except Exception as e:
        print(e)
    finally:
        conn.close()


master = Tk()
master2 = Tk

id = StringVar()
name = StringVar()

top = Frame(master, bg = 'yellow')
top.pack()

bottom = Frame(master)
bottom.pack(pady=5)

master.title("회원관리")
# master.geometry("190x250")
lbl_id = Label(top, text = "ID").grid(row=0, column=0)
txt_id = Entry(top, textvariable=id).grid(row=0, column=1, columnspan=3)
lbl_name = Label(top, text = "Name").grid(row=1, column=0)
txt_name = Entry(top, textvariable=name).grid(row=1, column=1, columnspan=3)
btn_add = Button(top, text="Add", command=addUser).grid(row=2, column=0)
btn_update = Button(top, text="Update", command=updateUser).grid(row=2, column=1)
btn_delete = Button(top, text="Delete", command=deleteUser).grid(row=2, column=2)
btn_list = Button(top, text="Search", command=selectUser).grid(row=2, column=3)

master.mainloop()