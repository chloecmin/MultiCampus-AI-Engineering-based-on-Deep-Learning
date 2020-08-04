# [파이썬 응용 프로그래밍]
# * 다음의 기능을 처리할 수 있는 코드를 작성하시오.
# 사칙연산을 사용한 계산기
# #######################
# # 1. 덧셈
# # 2. 뺄셈
# # 3. 곱셈
# # 4. 나눗셈
# # 5. 종료
# #######################
# 선택해주세요.(1-5) : 1
# 첫번째 숫자를 입력해주세요. : 20
# 첫번째 숫자를 입력해주세요. : 30
# 20 + 30 = 50

while(True):
    print("사칙연산을 사용한 계산기")
    print("#######################")
    print("1. 덧셈")
    print("2. 뺄셈")
    print("3. 곱셈")
    print("4. 나눗셈")
    print("5. 종료")
    print("#######################")
    op = int(input("선택해주세요.(1-5) : "))

    if op == 5:
        print("종료합니다.")
        break
    else:
        num1 = int(input("첫번째 숫자를 입력해주세요. : "))
        num2 = int(input("두번째 숫자를 입력해주세요. : "))
        if op == 1:
            ans = num1 + num2
            sign = '+'
        elif op == 2:
            ans = num1 - num2
            sign = '-'
        elif op == 3:
            ans = num1 * num2
            sign = '*'
        elif op == 4:
            ans = num1 / num2
            sign = '/'

        print("{} {} {} = {}".format(num1, sign, num2, ans))
