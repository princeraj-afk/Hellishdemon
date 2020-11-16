for _ in range(int(input())):
    ans = []
    n,W = [int(x) for x in input().split()]
    w = [int(x) for x in input().split()]
    if sum(w)>=W//2:
        i = 0
        while(W>0 and i<n):
            if w[i]<=W:
                ans.append(i+1)
            i+=1
        if len(ans)>0:
            print(len(ans))
            print(*ans)
        else:
            print(-1)
    else:
        print(-1)