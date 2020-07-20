class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "destroyed")

p1 = Point()
p2 = p1
p3 = p2

print(id(p1), id(p2), id(p3))

del p1
del p2
del p3
