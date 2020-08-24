for _ in range(int(input())):
    (a,b,c) = list(int(x) for x in input().split())
    (p,q,r) = list(int(x) for x in input().split())
    k = min(c,p)
    c -= k
    p -= k
    ans =k*2
    if c+a>=r:
        print(ans)
    else:
        print(ans-min(r-(a+c),b)*2)