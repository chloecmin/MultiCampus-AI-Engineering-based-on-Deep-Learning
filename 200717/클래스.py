# class vs object(instance)
# class -> instance
# variable..(init) -> constructor -> __init__
# variable..(destroy) -> destructor -> __del__

class Student:
    name = "홍길동"
    age = 20
    def gotoSchool(self): #self 는 현재객체 상태
        # print(self.name, self.age)
        pass

s=Student()
s.gotoSchool()

class Car:
    #속성
    name = ""
    color = ""
    speed = 0

    #동작
    def __init__(self, name, color, speed):
        self.name = name
        self.color = color
        self.speed = speed

    def upSpeed(self, value):
        self.speed += value
        print("현재 {}의 속도는 {}입니다.".format(self.name, self.speed))

    def downSpeedd(self, value):
        self.speed -= value
        print("현재 {}의 속도는 {}입니다.".format(self.name, self.speed))


c1 = Car("벤츠", "빨간색", 10)
# c1.name = "홍길동"
# c1.color = "빨간색"
# c1.speed = 10

c1.upSpeed(100)
# print("{} 차의 현재 속도는 {}입니다.".format(c1.name, c1.speed))
c1.downSpeedd(40)
# print("{} 차의 현재 속도는 {}입니다.".format(c1.name, c1.speed))