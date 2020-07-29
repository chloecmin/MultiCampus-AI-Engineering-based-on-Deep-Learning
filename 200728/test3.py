from array import *

# arr1 = array('i', [10, 20, 30, 40])
# for x in arr1:
#     print(x)
#
# arr1.insert(1, 100)
# print(arr1)
#
# arr1.remove(40)
# print(arr1)
##################################
# num1 = int(input("num1 : "))
# num2 = int(input("num2 : "))
# num3 = int(input("num3 : "))
# total = 0
#
# total = 0
# total += num1
# total += num2
# total += num3
# print(total)
##################################
# arr2 = [None]*3
#
# arr2[0] = int(input("num1 : "))
# arr2[1] = int(input("num2 : "))
# arr2[2] = int(input("num3 : "))
#
# sum2 = 0
# for i in arr2:
#     sum2 += i
# print(sum2)
##################################
# 배열 원소(3개)의 최대값을 구하시오.(입력을 3개 받는다.)
# arr3 = [None]*3
# arr3[0] = int(input("num1 : "))
# arr3[1] = int(input("num2 : "))
# arr3[2] = int(input("num3 : "))
#
# max = 0
# for i in arr3:
#     if i > max:
#         max = i
#
# print(max)
###################################
#함수 maxvalue(...)를 구현하시오.
def maxvalue(arr):
    max = 0
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max

print(maxvalue([100, 3, 4, 10, 20]))
print(maxvalue([100, 3, 4, 10, 20, 2, 3, 1, 1, 1]))



