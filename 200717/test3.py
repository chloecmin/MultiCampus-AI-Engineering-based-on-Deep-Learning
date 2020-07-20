"""클래스 상속"""

class Animal:
    def breathing(self):
        print("Animal breathing")
class Bird(Animal):
    def flying(self):
        print("Bird flying")
    def breathing(self): #Overriding (함수 이름과 옵션이 같음)
        print("Bird breathing")
class Dog(Animal):
    def barking(self):
        print("Dog barking")

bird = Bird()
bird.breathing()
bird.flying()

dog = Dog()
dog.breathing()
dog.barking()