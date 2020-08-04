# 1. 상자 최대 낙차 출력

box = [7, 4, 2, 0, 0, 6, 0, 7, 0]
boxli = []
maxvalue = 0
for heights in box:
    temp = []
    for h in range(heights):
        temp.append(1)
    for h in range(8-heights):
        temp.append(0)
    boxli.append(temp)

for i in range(len(boxli)-1):
    if boxli[0][i] == 1:
        cnt = 0
        for j in range(1, len(boxli)):
            if boxli[j][i] == 0:
                cnt += 1
        if cnt > maxvalue:
            maxvalue = cnt

print(maxvalue)