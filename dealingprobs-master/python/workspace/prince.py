a = int(input())
b = [int(x) for x in input().split()]
c = int(input())
d = [int(x) for x in input().split()]
e = (sum(b[:i+1]) for i in range(a))
print(*e)
for i in d:
    for j in e:
        print(i,j)
        if j>=i:
            break