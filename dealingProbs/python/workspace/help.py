for g in range(int(input())):
    n = int(input())
    d = {}
    for i in range(n):
        d[i]=0
    threshhold = (n-1)//2
    for i in range(n):
        for j in range(i+1,n):
            if d[i]<threshhold:
                print(1,end=" ")
                d[i]+=3
            elif d[j]<threshhold:
                print(-1,end=" ")
                d[j]+=3
            else:
                print(0,end=" ")
                d[i]+=1
                d[j]+=1
    print()