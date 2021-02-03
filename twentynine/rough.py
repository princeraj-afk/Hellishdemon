with open("rough.txt","r") as f:
    for _ in range(int(f.readline())):
        a,b = f.readline().split()
        p = set(list(a))
        q = set(list(b))
        r = p.difference(q)
        print(len(p),len(q),len(r))
        # if set(list(a)).difference(set(list(b))):
        #     print("Love you too")
        # else:
        # break
    #     print(f.readline())