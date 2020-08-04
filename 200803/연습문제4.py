# 4. 1부터 10,000까지 8이라는 숫자가 총 몇번 나오는가?
# 8이 포함되어 있는 숫자의 갯수를 카운팅 하는 것이 아니라 8이라는 숫자를 모두 카운팅 해야 한다.
# (※ 예를들어 8808은 3, 8888은 4로 카운팅 해야 함)

# 8이 한번나올 때 : 9*9*9 4
# 8이 두번나올 때 : 9*9 4*3/2*1
# 8이 세번나올 때 : 9 4*3*2/3*2*1
# 8이 네번나올 때 : 1

# 방법1
# eight_sum = 0
# for i in range(1, 4):
#     no_eight = 9**(4-i)
#     eight_cnt = 1
#     jmul = 1
#     for j in range(i):
#         eight_cnt *= (4-j)
#         jmul *= (j+1)
#     eight = eight_cnt//jmul
#     eight_sum += no_eight*eight*i
#
# answer = eight_sum+4
# print(answer)

# #방법2
# cnt = 0
# for i in range(1, 10000):
#     for j in str(i):
#         if '8' == j:
#             cnt += 1
# print(cnt)

# 방법3
print(str(list(range(1, 10001))).count('8'))