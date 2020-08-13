m,n,a,b = list(int(x) for x in input().split())
print(a,b)
print(a,1)
for i in range(1,m+1,2):
    for j in range(1,n+1):
        if (i,j)!=(a,b) and (i,j)!=(a,1):
            print(i,j)
        else:
            pass
    i+=1
    for j in range(n,0,-1):
        if (i,j)!=(a,b) and (i,j)!=(a,1):
            print(i,j)
        else:
            pass
for _ in range(m%2):
    for j in range(1,n+1):
        i = m
        if (i, j) != (a, b) and (i, j) != (a, 1):
            print(i, j)
        else:
            pass