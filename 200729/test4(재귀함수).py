# data = [1,2,3,4]
# sum2 = 0
# for i in data:
#     sum2 += i
# print(sum2)

# def sum3(data):
#     if len(data) == 1:
#         return data[0]
#     else:
#         return data[0]+sum3(data[1:])
# print(sum3(data))

#n!
# n = 5
# factorial = 1
# for i in range(1,n+1):
#     factorial = factorial * i
# print(factorial)

#재귀함수, recurssion
def factorial(n):
    if n == 1:
        return 1
    elif n < 0:
        return 0
    else:
        return n*factorial(n-1)
print(factorial(5))


