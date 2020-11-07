t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    j=n-1
    while j>0 and a[j-1]>=a[j]:
        j-=1
    while j>0 and a[j-1]<=a[j]:
        j-=1
    print(j)