"""key와 value이용한(dic타입) 가변 파라미터 (**)"""

def printPersons(**info):
    print(type(info))
    print(info)

printPersons(name = '홍길동', age = 20, hobby = '농구')