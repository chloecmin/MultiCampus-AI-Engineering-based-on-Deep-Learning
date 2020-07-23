def test(x):
    return x>10

def filter2(func, list1):
    list2 = []
    for i in list1:
        if func(i): #콜백함수
            list2.append(i)
    return list2

print(filter2(test, [20, 100, 30, -1]))
print(list(filter(lambda x:x>10, [20, 100, 30, -1])))