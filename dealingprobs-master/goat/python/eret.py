n=4646
i=0
print("Goodluck! you have 19 chances to guess the number.")
a=int(input("Enter the number\n"))
while(a!=n) and i<18:
    print ("Chances left:",18-i)
    if a>n:
        print("Greater than actual number!")
    if a<n:
        print ("Lesser than actual number!")
    a=int (input ("Enter the number"))
    i=i+1
    continue
if a==n:
    print("Congrats, u got the number in:",i+1,"th time")
else:
    print("Sorry u loose!")