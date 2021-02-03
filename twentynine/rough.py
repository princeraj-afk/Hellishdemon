with open("rough.txt","r") as f:
    for _ in range(int(f.readline())):
        a,b = f.readline().split()
        p = set(list(a))
        q = set(list(b))
        r = p.difference(q)
        print(len(p),len(q),len(r))