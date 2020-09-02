a,b = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]
d = [i>=c[b-1] and i>0 for i in c]
print(d.count(True))