import sqlite3

class userMgr:
    def getUser(self, name):
        try:
            self.conn = sqlite3.connect("C:\\sqlite\\test.db")
            print("Opened database successfully")

            if name == "*":
                self.sql = "SELECT * FROM emp"
            else:
                self.sql = "SELECT * FROM emp WHERE NAME = \'{}\'".format(name)

            self.cursor = self.conn.execute(self.sql)
            self.emps = self.cursor.fetchall()

            # print(self.emps)

            # for self.emp in self.emps:
            #     print(self.emp)

            for (self.id, self.name) in self.emps:
                print(self.id, self.name)
        except Exception as e:
            print(e)
        finally:
            self.conn.close()
    def addUser(self, id, name):
        try:
            check = 0
            self.conn = sqlite3.connect("C:\\sqlite\\test.db")
            print("Opened database successfully")

            self.sql = "SELECT * FROM emp"
            self.cursor = self.conn.execute(self.sql)
            self.emps = self.cursor.fetchall()

            for self.emp in self.emps:
                print(self.emp[0], self.emp[1])
                if self.emp[0] == id or self.emp[1] == name:
                    print("중복되는 ID나 이름이 있습니다.")
                    check = 1
                    break

            if check == 0:
                self.sql2 = "INSERT INTO emp VALUES ({}, \'{}\')".format(id, name)

                self.conn.execute(self.sql2)
                self.conn.commit()
                print("추가되었습니다.")
        except Exception as e:
            print(e)
        finally:
            self.conn.close()
    def updateUser(self, name, newname):
        try:
            self.conn = sqlite3.connect("C:\\sqlite\\test.db")
            print("Opened database successfully")

            self.sql = "UPDATE emp SET NAME=\'{}\' WHERE NAME=\'{}\'".format(newname, name)

            self.conn.execute(self.sql)
            self.conn.commit()
            print("수정되었습니다.")
        except Exception as e:
            print(e)
        finally:
            self.conn.close()
    def deleteUser(self, name):
        try:
            self.conn = sqlite3.connect("C:\\sqlite\\test.db")
            print("Opened database successfully")

            self.sql = "DELETE FROM emp WHERE NAME=\'{}\'".format(name)

            self.conn.execute(self.sql)
            self.conn.commit()
            print("삭제되었습니다.")
        except Exception as e:
            print(e)
        finally:
            self.conn.close()

if __name__ == '__main__':
    userMgr = userMgr()
    while True:
        print("# 회원관리 ")
        print("#########################")
        print(" 1. 전체회원검색")
        print(" 2. 회원검색")
        print(" 3. 회원추가")
        print(" 4. 회원수정")
        print(" 5. 회원삭제")
        print(" 6. 종료")
        print("#########################")
        option = input("메뉴를 선택해주세요.(1-6): ")
        if option == "1":
            userMgr.getUser("*")
        elif option == "2":
            userMgr.getUser(input("회원명을 입력해주세요. : "))
        elif option == "3":
            # userMgr.addUser(input("Id를 입력해주세요. : "), input("회원명을 입력해주세요. : "))
            idinput, nameinput = input("ID와 회원명을 입력해주세요. : ").split()
            userMgr.addUser(idinput, nameinput)
        elif option == "4":
            userMgr.updateUser(input("회원명을 입력해주세요. : "), input("새회원명을 입력해주세요. : "))
        elif option == "5":
            userMgr.deleteUser(input("회원명을 입력해주세요. : "))
        elif option == "6":
            print("감사합니다. 수고하십시요.")
            break
        else:
            print("잘못입력하셨습니다. 다시 확인 부탁드립니다.")
            break

