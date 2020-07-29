# 다음에 제공되는 데이터에 값이 존재하는지 검색하시오.
# 결과는 True, False

def searchElement(list, num):
    if num in list:
        return True
    else:
        return False

print(searchElement([10,2,3,4,5,5,3], 3))
print(searchElement([10,2,3,4,5], 6))