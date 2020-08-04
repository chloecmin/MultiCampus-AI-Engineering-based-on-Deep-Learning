# def generator_test():
#     yield 1
#     yield '2'
#     yield 'test'
#
# # 호출하는 방법 1
# for i in generator_test():
#     print(i)
#
# # 호출하는 방법 2
# d = generator_test()
# print(d.__next__())
# print(d.__next__())
# print(d.__next__())

def num_generator(n):
    num = 1
    while True:
        yield num
        if num == n:
            return
        else:
            num += 1
for i in num_generator(10):
    print(i)
