a = input("a : ") #문자열
b = input("b : ") #문자열
op = input("op : ") #문자열

print(type(a), type(b), type(op))
c = a+op+b
d = eval(c) # eval : 문자열을 수식으로 변환하여 계산
print(d)