from functools import reduce
def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
for _ in range(int(input())):
    n,x,y = [int(x) for x in input().split()]
    p = factors(y-x)
    q = []
    for i in p:
        if i<=(y-x)//(n-1):
            q.append(i)
    print(q)