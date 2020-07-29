#Bubble Sorting : 가장 큰 데이터를 가장 뒤로 보내며 정렬하는 방식이다.

data = [15, 11, 1, 3, 8]

# for _ in range(len(data)):
#     for i in range(len(data)-1):
#         if data[i] > data[i+1]:
#             temp = data[i]
#             data[i] = data[i+1]
#             data[i+1] = temp
for p in range(len(data)-1, 0, -1):
    for i in range(p):
        if data[i] > data[i + 1]:
            temp = data[i]
            data[i] = data[i + 1]
            data[i + 1] = temp

print(data)