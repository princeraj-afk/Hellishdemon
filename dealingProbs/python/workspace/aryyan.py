s = []
for i in range(10):
    for j in range(10):
        for k in range(10):
            if (i+j+k)%9==0:
                s.append((i,j,k))
print(len(s))