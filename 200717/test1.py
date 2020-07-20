class person:
    name = ""
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walking(self):
        print("{} 걷는다.".format(self.name))

class person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def add_age(self, num):
        self.age += num
        print("{}년 후 나이는 {}입니다.".format(num, self.age))

p = person("홍길동", 20)
p.walking()

p2 = person2("이순신", 40)
p2.add_age(5)