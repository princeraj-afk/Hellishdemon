from collections import Counter
n = int(input())
a = sorted(map(int,input().split()))
k = []
for i in range(n):
    for j in range(i+1,n):
        if a[j]==a[i]:
            pass
        elif a[j]-a[i]==1:
            k.append(i)
            k.append(j)
        else:
            break
g = Counter(k).values()
ans = [(i*(i-1))//2 for i in g]
print(sum(ans)+sum(g)//2)