s =[9, 5, 2, 7, 3, 20, 100, 95]

s.sort()
min_dist = 100
for i in range(len(s)-1):
    p1, p2 = s[i], s[i+1]
    if min_dist > abs(p1 - p2):
        min_dist = abs(p1 - p2)
        dist_a, dist_b = p1, p2
print(dist_a, dist_b)