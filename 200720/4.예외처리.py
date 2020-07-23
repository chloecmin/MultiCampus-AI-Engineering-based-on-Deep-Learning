# try:
#     a = int(input("a : "))
#     b = int(input("b : "))
#     c = a/b
#     print("a/b = {}".format(c))
#
# except ZeroDivisionError as e:
#     print(e,": 0으로 나눌 수 없음")
# else:
#     print("값은 : {}".format(c))

#########################################
try:
    f = open("..\\textfiles\\test.txt", "r", encoding='utf-8')
except:
    f = open("..\\textfiles\\test.txt", "w", encoding='utf-8')
    f.write("안녕")
    print("created a file")
finally:
    f.close()