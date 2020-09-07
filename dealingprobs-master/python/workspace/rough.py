from itertools import permutations

def fingerprint(arr):
    g = []
    for i in range(len(arr)-1):
        g.append(arr[i]+arr[i+1])
    return g

for _ in range(int(input())):
    a = int(input())
    b= [int(x) for x in input().split()]
    for i in permutations(b,a):
        if fingerprint(i)==fingerprint(b) and i!=b:
            print(*i)
            break