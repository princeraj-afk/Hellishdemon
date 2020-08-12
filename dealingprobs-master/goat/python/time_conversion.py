l = input()
hour = l[:2]
miu = l[3:5]
sec = l[6:8]
dod = l[8:]
if int(hour) == 12:
    hour = "00"
else:
    pass
if dod =="AM":
    print(hour,end=":")
    print(miu,end=":")
    print(sec,end="")
else:
    print (int(hour)+12, end=":")
    print (miu, end=":")
    print (sec, end="")