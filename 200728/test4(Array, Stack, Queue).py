#배열 역으로 정렬
#[10, 2, 3, 4, 5] -> [5, 4, 3, 2, 10]

# # 1.
# def reverseArr(list):
#     list.reverse()
#     return list
#
# # 2.
# def reverseArr2(list):
#     list_rev = []
#     for l in list[::-1]:
#         list_rev.append(l)
#     return list_rev
#
# list = [10, 2, 3, 4, 5]
# # print(reverseArr(list))
# print(reverseArr2(list))


# t = [[1,2,3,4],[3,4,5,6],[4,5,6,3],[4,5,3,2]]
# for i in t:
#     for j in i:
#         print(j, end=" ")
#     print("")

# import numpy as np
#
# d = np.array([1,2,3,4])
# print(d)
#
# d2 = np.array([[1,2,3,4],[2,3,4,6],[5,6,8,9]]) #3x4 matrix
# print(d2)
# print(d2[0])
# print(d2[0][1])
# print(d2.shape)


# from numpy import *
#
# d = array([1,2,3,4])
# print(d)
#
# d2 = array([[1,2,3,4],[2,3,4,6],[5,6,8,9]]) #3x4 matrix
# print(d2)
# print(d2.shape)
# print(reshape(d2, (4,3)))


# import collections
#
# d3 = {'day1':'mon', 'day2':'tue'}
# d4 = {'day3':'wed', 'day4':'thu'}
#
# r = collections.ChainMap(d3, d4)
# print(r.maps, "\n")
#
# print(list(r.keys()), list(r.values()))


# class Stack:
#     def __init__(self):
#         self.stack = []
#     def push(self, v):
#         self.stack.append(v)
#     def pop(self):
#         return self.stack.pop()
#     def peek(self):
#         return  self.stack[-1]
# s = Stack()
# s.push(1)
# s.push(2)
# s.push(3)
# s.push(4)
# print(s.pop())
# print(s.pop())
# print(s.peek())
# print(s.peek())


class Queue:
    def __init__(self):
        self.queue = list()
    def insert(self, value):
        self.queue.insert(0, value)
    def size(self):
        return len(self.queue)
    def remove(self):
        return self.queue.pop()

q = Queue()
q.insert('Mon')
q.insert('Tue')
q.insert('Wed')
print(q.size())
print(q.remove())
print(q.remove())
