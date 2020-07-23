def SayHello(name):
    print("Hello {} Nice to meet you".format(name))
    return 0

if __name__ == "__main__": #단독으로 해당 파일에서만 단독으로 수행할 때 사용. 모듈로 사용 시 실행 안됌.
    print("__name__", __name__)
    SayHello("강감찬")
