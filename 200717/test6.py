class Student:
    #생성자 오버로딩(Constructor Overloading) -> 같은 이름의 메소드를 사용하면서 파라미터의 개수가 다른 것
    def __init__(self, name = '', age = 0):
        self.name = name
        self.age = age
    def studying(self):
        if self.age == 0 and self.name == '':
            print(None)
        else:
            print(self.name, self.age)

s = Student()
s1 = Student('홍길동')
s2 = Student('이순신', 30)

s.studying()
s1.studying()
s2.studying()

s.name = '이성계'
s.age = 10
s.studying()

s1.age = 20
s1.studying()