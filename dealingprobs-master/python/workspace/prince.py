for _ in range(int(input())):
    a,b = [int(x) for x in input().split()]
    c = [int(x)%2 for x in input().split()]
    d = (c.count(1),c.count(0))
    k = max(d[1],b-1)
    if d[0]>=b-k:
        print("Yes")
    else:
        print('No')