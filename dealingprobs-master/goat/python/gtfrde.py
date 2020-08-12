#sibunoichi series
def sib(n):
    if n==0:
        yield 0
    if n==1:
        yield 1
    else:
        yield sib(n-1)+sib(n-2)
s = sib(8)
print(s)

def fact(i):
    if i==0:
        yield 1
    if i==1:
        yield 1
    else:
        yield i*fact(i-1)
t= fact(9)
print(t)
f = (j for j in range(8))
print(f)
