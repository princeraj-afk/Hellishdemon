f= open("luc 1.txt","r",encoding="utf8")
p = f.read()
for i in p[:]:
    print(i)
    if i in list("1234567890,.:")+["\n","\r","(",")","/"]:
        p.replace(i,"")
k = set(p.split(" "))
for i in k:
    print(i)