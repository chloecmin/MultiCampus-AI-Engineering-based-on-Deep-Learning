f = open("test.txt", "w") #쓰기 #한글일 때 옵션 : encoding="UTF-8"
for i in range(1, 11):
    data = "{} Data\n".format(i)
    f.write(data)
f.close()

f2 = open("test.txt", "r") #읽기
# print(f2.readline())
while 1:
    line = f2.readline()
    if not line: break
    # print(line)
f2.close()

f3 = open("test.txt", "r") #읽기
lines = f3.readlines()
for line in lines:
    # print(line)
    pass
f3.close()

f4 = open("test.txt", "a") #쓰기-옵션 a(텍스트 추가), 옵션 w(오버라이트)
for i in range(11, 31):
    data = "{}'s input\n".format(i)
    f4.write(data)
f4.close()