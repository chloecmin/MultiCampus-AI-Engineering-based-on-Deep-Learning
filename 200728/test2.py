# n = int(input("n값을 입력해주세요 : "))
#
# i = 1
# sum = 0
# while i <= n:
#     sum += i
#     i += 1
#
# print(sum)

str1 = "%s is %s" % ("Hello", "Python")
str2 = "{} is {}".format("Hello", "Python")

""" f-문자열 """
name = "이순신"
age = 30
fstr3 = f'{name}의 나이는 {age}'
print(fstr3)

#변경될 수 있는 타입 : list, dictionary, set
#변경될 수 없는 타입 : numeric, string, tuple