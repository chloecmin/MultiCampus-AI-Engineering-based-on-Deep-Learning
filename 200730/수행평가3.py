# [파이썬 알고리즘]
# * 사원을 정보를 txt파일로 관리할 수있는 프로그램을 작성하시오.
# (File IO을 사용하여 구현하시오.)
# # 사원관리
# #########################
# 1. 전체사원검색
# 2. 사원검색
# 3. 사원검색(다중검색)
# 4. 사원추가
# 5. 사원수정
# 6. 사원삭제
# 7. 종료
# #########################
# 메뉴를 선택해주세요.(1-6):
#
# 데이터 파일은 emps.txt를 생성하여 관리하시오.
# 3. 사원검색(다중검색)
# 입력시 : 이순신, 강감찬 <- 형식으로 입력시 처리함

import os

class EmpManager:
    def existFile(self):
        if os.path.exists("emps.txt"):
            pass
        else:
            self.f = open("emps.txt", "w", encoding="utf-8")
            self.f.close()
            print("emps.txt 파일이 존재하지 않아 생성하였습니다.")
    def getEmp(self):
        self.existFile()
        self.f = open("emps.txt", 'r', encoding='utf-8')
        self.namelist = self.f.readlines()
        for self.name in self.namelist:
            print(self.name.replace("\n", ""))
        self.f.close()
    def getEmpByName(self, name):
        self.existFile()
        self.emp = name
        self.f = open('emps.txt', 'r', encoding='utf-8')
        self.namelist = self.f.readlines()
        self.check = False
        for self.name in self.namelist:
            self.name = self.name.replace("\n", "")
            if self.name == self.emp:
                self.check = True
                break
        if self.check:
            print("[{}] 사원은 존재합니다.".format(self.emp))
        else:
            print("[{}] 사원은 존재하지 않습니다.".format(self.emp))

        self.f.close()
    def getMultipleEmpByName(self, names):
        self.existFile()
        self.emplist = list(names.split(", "))
        self.f = open('emps.txt', 'r', encoding='utf-8')
        self.namelist = self.f.readlines()

        for self.emp in self.emplist:
            self.check = False
            for self.name in self.namelist:
                self.name = self.name.replace("\n", "")
                if self.name == self.emp:
                    self.check = True
                    break
            if self.check:
                print("[{}] 사원은 존재합니다.".format(self.emp))
            else:
                print("[{}] 사원은 존재하지 않습니다.".format(self.emp))
        self.f.close()
    def createEmp(self, name):
        self.existFile()
        self.emp = name
        self.f = open("emps.txt", "r", encoding="utf-8")
        self.namelist = self.f.readlines()
        self.f.close()
        self.f = open("emps.txt", "w", encoding='utf-8')

        for self.name in self.namelist:
            self.f.write(self.name)

        self.f.write(self.emp + "\n")
        self.f.close()
        print("[{}] 사원을 추가하였습니다.".format(self.emp))
    def updateEmp(self, name, new_name):
        self.existFile()
        self.emp = name
        self.f = open('emps.txt', 'r', encoding='utf-8')
        self.namelist = self.f.readlines()
        self.check = False
        for self.name in self.namelist:
            self.name = self.name.replace("\n", "")
            if self.name == self.emp:
                self.check = True
                break
        if self.check == False:
            print("[{}] 사원이 존재하지 않아 수정할 수 없습니다.".format(self.emp))
        else:
            self.new_name = new_name
            # self.f = open("emps.txt", 'r', encoding='utf-8')
            # self.namelist = self.f.readlines()
            self.f.close()
            self.f = open("emps.txt", 'w', encoding="utf-8")
            for self.name in self.namelist:
                self.name = self.name.replace("\n", "")
                if self.name == self.emp:
                    self.name = self.new_name
                self.f.write(self.name + "\n")
            self.f.close()
            print("[{}] 사원을 [{}] 사원으로 수정하였습니다.".format(name, new_name))
    def deleteEmp(self, name):
        self.existFile()
        self.emp = name
        self.f = open("emps.txt", 'r', encoding='utf-8')
        self.namelist = self.f.readlines()
        self.f.close()
        self.f = open("emps.txt", 'w', encoding="utf-8")
        for self.name in self.namelist:
            self.name = self.name.replace("\n", "")
            if self.name == self.emp: continue
            self.f.write(self.name + "\n")
        self.f.close()
        print("[{}] 사원을 삭제하였습니다.".format(self.emp))
class AppManager:
    def run(self):
        self.em = EmpManager()

        while True:
            print("# 사원관리 ")
            print("#########################")
            print(" 1. 전체사원검색")
            print(" 2. 사원검색")
            print(" 3. 사원검색(다중검색)")
            print(" 4. 사원추가")
            print(" 5. 사원수정")
            print(" 6. 회원삭제")
            print(" 7. 종료")
            print("#########################")
            op = input("메뉴를 선택해주세요.(1-7): ")
            if op == "1":
                self.em.getEmp()
            elif op == "2":
                self.name = input("사원명을 입력해주세요. : ")
                print("")
                self.em.getEmpByName(self.name)
            elif op == "3":
                self.name = input("사원명(다중)을 입력해주세요. : ")
                print("")
                self.em.getMultipleEmpByName(self.name)
            elif op == "4":
                self.name = input("사원명을 입력해주세요. : ")
                print("")
                self.em.createEmp(self.name)
            elif op == "5":
                self.name = input("사원명을 입력해주세요. : ")
                self.new_name = input("새 사원명을 입력해주세요. : ")
                print("")
                self.em.updateEmp(self.name, self.new_name)
            elif op == "6":
                self.name = input("사원명을 입력해주세요. : ")
                print("")
                self.em.deleteEmp(self.name)
            elif op == "7":
                print("종료합니다.")
                break
            else:
                print("잘못입력하셨습니다.")
                break
            print("")

if __name__ == "__main__":
    try:
        app = AppManager()
        app.run()
    except Exception as e:
        print(e)