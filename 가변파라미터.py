#가변 파라미터
def printNames(*names):
    for name in names:
        print(name)
    print("------------------이번 함수 실행 끝")
    return

printNames('이순신', '홍길동', '이순신')
printNames('강감찬', '권율')