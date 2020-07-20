class Line:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, other):
        return Line(self.a + other.a, self.b + other.b)

if __name__ == '__main__':
    l1 = Line(1,2)
    l2 = Line(3,4)

    l3 = l1.__add__(l2)
    print(l3.a, l3.b)