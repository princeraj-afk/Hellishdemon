b=1
while(b==1):
    n=int(input("Enter the value of n\n"))
    a=int(input("enter 0 for False and 1 for True\n"))
    if bool(a):
        for i in range(1,n+1):
            for j in range(1,i+1):
                print("😎",end="")
            print()

    else:
        for i in range(1,n+1):
            for j in range(1,n+2-i):
                print("*",end="")
            print()
    b=int(input("press 1 to continue and 0 to exit"))
    if b==1:
        'continue'
    else: 'break'