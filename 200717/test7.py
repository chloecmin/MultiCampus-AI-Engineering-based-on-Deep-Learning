class Employee: #캡슐화(data hide) : __변수 ->변수에 바로 접근하지 못하도록 함수로 캡슐화
    __test = 10 #private variable
    def __test2(self): #private fucntion
        pass
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def getName(self):
        return  self.__name
    def getAge(self):
        return self.__age
    def setName(self, name):
        self.__name = name
    def setAge(self, age):
        self.__age = age

e = Employee("이순신", 30)
print(e.getName(), e.getAge())