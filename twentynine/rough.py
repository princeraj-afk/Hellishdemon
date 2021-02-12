a = int(input())
s = set()
for _ in range(a):
    x1,y1,x2,y2 = [int(x) for x in input().split()]
    for i in range(x1,x2):
        for j in range(y1,y2):
            s.add((i,j))
print(len(s))