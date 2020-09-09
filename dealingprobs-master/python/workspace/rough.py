with open("D:\\Meredian\\dealingprobs-master\\python\\int. python\\urls1.txt","r+") as f:
    for i in f:
        k = sorted(i.split(", "))
        with open("./otherthing.txt","a") as p:
            for l in k:
                p.write(l+"\n")