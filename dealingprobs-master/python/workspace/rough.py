def median(arr):
    p = len(arr)
    if p % 2 == 1:
        return arr[p // 2]
    else:
        return (arr[p // 2] + arr[p // 2 - 1]) // 2


a = int(input())
b = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]
d = []
for i in range(a):
    p = [b[i] for i in range(c[i])]
    d += p
    d = []

d.sort()

if a % 2 == 0:
    first_q = median(b[:a // 2])
    second_q = median(b)
    third_q = median(b[a // 2:])
else:
    first_q = median(b[:a // 2])
    second_q = median(b)
    third_q = median(b[a // 2 + 1:])

print(third_q - first_q)