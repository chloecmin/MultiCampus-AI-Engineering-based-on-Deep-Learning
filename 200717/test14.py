class Point:
    def __init__(self, a):
        self.a = a
    def __add__(self, other): #매직메소드
        return self.a + other.a
    def add(self, p2):
        # r = self.a + p2.a
        # p3 = Point(r)
        # return p3
        return Point(self.a + p2.a).a

p1 = Point(1)
p2 = Point(2)

print(p1+p2) # = p1.__add__(p2)
print(p1.add(p2))