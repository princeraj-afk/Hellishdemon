import numpy
a = int(input())
b = []
for i in range(a):
    b.append([float(x) for x in input().split()])
b = numpy.array(b)
print(format(numpy.linalg.det(b),".2f"))

import numpy
print(round(numpy.linalg.det(numpy.array([list(map(float,input().split())) for _ in range(int(input()))])),2))