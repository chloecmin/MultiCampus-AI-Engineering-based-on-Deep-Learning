"""가변 파라미터(튜플이용)"""

# def printNames(*names): #튜플형태로 입력
#     for name in names:
#         print(name)
#     print("------------------이번 함수 실행 끝")
#     return
#
# printNames('이순신', '홍길동', '이순신')
# printNames('강감찬', '권율')

def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum+i
    return sum

print(sum_many(1,2,3,4,5))
print(sum_many(10, 20))