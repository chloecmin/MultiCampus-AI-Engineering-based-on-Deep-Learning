class Car:
    def __init__(self, speed):
        self.speed = speed

    def speedup(self, speed):
        self.speed += speed
        print("class car에서 속도 업")

class Truck(Car):
    def speedup(self): #overloading
        self.speed += 10
        print("현재 속도는 {}입니다.".format(self.speed))

car = Truck(10)
car.speedup()

car2 = Car(10)
car2.speedup(20)