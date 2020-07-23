def test(x):
    return x*2

def map2(func, list1):
    list2 = []
    for i in list1:
        list2.append(func(i))
    return list2

print(map2(test, [1,2,3,4]))
print(list(map(lambda x : x*2, [1,2,3,4])))