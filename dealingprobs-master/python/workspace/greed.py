g1 = [0]
g2 = [0]
h1 = [0]
h2 = [0]
p = int(input())
for _ in range(p):
    a, b = [int(x) for x in input().split()]
    g1.append(a)
    h1.append(b)
for i in range(1,p+1):
    g2.append(g1[i]-g1[i-1])
    h2.append(h1[i]-h1[i-1])
g2.pop(0)
h2.pop(0)
print(g2,h2)