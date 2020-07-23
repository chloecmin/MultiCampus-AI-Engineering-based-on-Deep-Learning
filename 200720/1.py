#Overloading(Class only) vs Overriding(Class inheritance)
#접근자 : public, private(__), protected(_)
class Person5:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def getName(self):
        return self.__name
    def setName(self, name):
        self.__name = name
    def getAge(self):
        return self.__age
    def setAge(self, age):
        self.__age = age

p = Person5("이순신", 23)
print(p.getName(), p.getAge())