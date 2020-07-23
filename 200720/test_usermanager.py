class ManageUsers:
    def search(self, name):
        self.file = open("..\\textfiles\\users.txt", "r", encoding='utf-8')
        self.namelist = self.file.readlines()

        for self.n in self.namelist:
            if name == "*" : print(self.n.replace("\n", ""))
            elif self.n.strip() == name : print("{}님이 있습니다.".format(name))

        self.file.close()
    def add(self, name):
        self.file = open("..\\textfiles\\users.txt", "a", encoding='utf-8')
        self.file.write(name)
        self.file.write("\n")
        self.file.close()
    def change(self, orig_name, ch_name):
        self.file = open("..\\textfiles\\users.txt", "r+", encoding='utf-8')
        self.namelist = self.file.readlines()
        self.file.close()

        self.file = open("..\\textfiles\\users.txt", "w", encoding='utf-8')
        for self.n in self.namelist:
            if self.n.strip() == orig_name:
                self.file.write(ch_name)
                # n.replace("\n", "") == ch_name
                self.file.write("\n")
            else:
                self.file.write(self.n.strip())
                self.file.write("\n")
        self.file.close()
    def delete(self, name):
        self.file = open("..\\textfiles\\users.txt", "r", encoding='utf-8')
        self.namelist = self.file.readlines()
        self.file.close()

        self.file = open("..\\textfiles\\users.txt", "w", encoding='utf-8')
        d_name = name+"\n"

        for self.n in self.namelist:
            if self.n != d_name:
                self.file.write(self.n)
        self.file.close()

class App:
    def run(self):
        self.mu = ManageUsers()

        while(1):

            # print("# 회원관리")
            # print("####################")
            # print("1. 전체회원검색\n2. 회원검색\n3. 회원추가\n4. 회원수정\n5.회원삭제\n6. 종료\n")
            # print("####################")
            self.option = int(input("메뉴를 선택해주세요.(1-6) : "))

            if self.option == 1:
                self.mu.search('*')
            elif self.option == 2:
                self.mu.search(input("검색할 이름을 입력하세요 : "))
            elif self.option == 3:
                self.mu.add(input("추가할 이름을 입력하세요 : "))
            elif self.option == 4:
                self.mu.change(input("회원을 선택하세요 : "), input("수정 할 이름을 입력 : "))
            elif self.option == 5:
                self.mu.delete(input("삭제할 회원을 고르세요 : "))
            elif self.option == 6:
                break

if __name__ == '__main__':
    app = App()
    app.run()


