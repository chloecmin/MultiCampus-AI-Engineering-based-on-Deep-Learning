class Stack:
    def __init__(self):
        self.stack = list()
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
        return self.stack
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def getStack(self):
        return self.stack

s = Stack()
print(s.isEmpty())
s.push(1)
s.push(2)
s.push(3)
print(s.isEmpty())
print(s.pop())
print(s.peek())
print(s)
print(s.getStack())
