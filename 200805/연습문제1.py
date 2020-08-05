def s(li):
    return (li[2]-li[0])*(li[3]-li[1])

def square(s1, s2):
    # if (s2[0]>s1[0] and s2[0]<s1[2]) or (s1[0]>s2[0] and s1[0]<s2[2]):
    #     print("겹친다")
    #     x1, y1 = max(s1[0], s2[0]), max(s1[1], s2[1])
    #     x2, y2 = min(s1[2], s2[2]), min(s1[3], s2[3])
    #     print(x1, y1, x2, y2)
    #     print(s([x1, y1, x2, y2]))
    #     return s([x1, y1, x2, y2])
    # elif (s2[3]>s1[1] and s2[3]<s1[3]) or (s1[3]>s2[1] and s1[3]<s2[3]):
    #     print("겹친다")
    #     x1, y1 = max(s1[0], s2[0]), max(s1[1], s2[1])
    #     x2, y2 = min(s1[2], s2[2]), min(s1[3], s2[3])
    #     print(x1, y1, x2, y2)
    #     print(s([x1, y1, x2, y2]))
    #     return s([x1, y1, x2, y2])
    # else:
    #     return 0
    x1, y1 = max(s1[0], s2[0]), max(s1[1], s2[1])
    x2, y2 = min(s1[2], s2[2]), min(s1[3], s2[3])
    if s([x1, y1, x2, y2])>0:
        print(s([x1, y1, x2, y2]))
        return s([x1, y1, x2, y2])
    else:
        print(0)
        return 0



input = [[1,2,4,4], [2,3,5,7], [3,1,6,5],[7,3,8,6]]

same_s = 0
sep_s = 0
for i in range(len(input)):
    print("넓이 : ", s(input[i]))
    for j in range(i+1, len(input)):
        same_s += square(input[i], input[j])
    sep_s += s(input[i])
print(sep_s)
print(same_s)
print(sep_s-same_s)
