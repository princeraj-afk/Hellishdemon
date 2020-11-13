def wave_sort(a):
    k = len(a)//2
    p = sorted(a)
    p1 = p[:k]
    p2 = p[k:]
    a.clear()
    for i in range(k):
        a.append(p2[i])
        a.append(p1[i])
    a.append(max(p))
    a[0] = 90

g = [1, 2, 34, 4, 5, 5, 5, 65, 6, 65, 5454, 4]
wave_sort(g)
print(g)
# [1, 2, 34, 4, 5, 5, 5, 65, 6, 65, 5454, 4]