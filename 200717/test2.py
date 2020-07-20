class Employee:
    empCount = 0
    emplist = []
    def __init__(self, name, salary): #클래스 초기화
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        Employee.emplist.append([self.name, self.salary])

    def display_Count(self):
        print(Employee.empCount)
    def display_Employee(self):
        print(self.name, self.salary)

    def __del__(self): #객체 소멸
        class_name = self.__class__.__name__
        print(class_name, "destroyed")

emp1 = Employee("이순신", 3000)
emp1.display_Count()
emp1.display_Employee()
emp1.__del__()

emp2 = Employee("홍길동", 2000)
emp2.display_Count()
emp2.display_Employee()

for emp in Employee.emplist:
    print(emp)
