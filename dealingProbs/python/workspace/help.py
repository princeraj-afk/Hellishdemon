a , b = [int(x) for x in input().split()]
lol = []
for _ in range(a):
    lol.append(list(input()))

for i in range(a):
    for j in range(b):
        if lol[i][j] == ".":
            if (i + j) % 2 == 0:
                lol[i][j]='B'
            else:
                lol[i][j]='W'
for i in range(a):
    print("".join(lol[i]))