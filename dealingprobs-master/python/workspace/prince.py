a = []
m = []
for _ in range(6):
    a.append([int(x) for x in input().split()])
for i in range(4):
    for j in range(4):
        p1 = sum([a[i][j+p] for p in range(3)])
        p2 = a[i+1][j+1]
        p3 = sum([a[i+2][j+p] for p in range(3)])
        m.append(p1+p2+p3)
print(max(m))