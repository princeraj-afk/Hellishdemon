a = input("enter first number")
a = int(a)
b = input("enter second number")
b = int(b)
choice = input("enter operator")

if  (choice== "+"):
    if (a==56 and b==9 or b==56 and a==9):
        print ("77")
    else:
        print (a+b)

elif (choice=="-"):
    print (a-b)
elif (choice=="/"):
    if (a==56 and b==6 or b==56 and a==6):

        print ("4")
    else:
     print(a/b)
elif (choice=="*"):
    if (a==45 and b==3 or a==3 and b==45):
        print ("555")
    else:
     print (a*b)
else:
    print("invalid")