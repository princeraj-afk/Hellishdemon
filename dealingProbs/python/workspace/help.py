def prime(n):
    if n==1:
        return False
    for i in range (2, n):
        if n % i == 0:
            return False
    return True

a = int(input())
b = [int(x) for x in input().split()]
for j in b:
    if (j**0.5)%1==0 and prime(int(j**0.5)):
        print("YES")
        continue
    print("NO")