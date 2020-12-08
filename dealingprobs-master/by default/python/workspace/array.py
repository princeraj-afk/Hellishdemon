n=56
i=0
print("Goodluck! you have 9 chances to guess the number.")
print("Enter the number")
a=int(input())
while(a!=n) and i<8:
    print ("Chances left:",8-i)
    if a>n:
        print("Greater than actual number!")
    if a<n:
        print ("Lesser than actual number!")
    print ("Enter the number")
    a=int (input ())
    i=i+1
    continue
if a==n:
    print("Congrats, u got the number!")
else:
    print("Sorry u loose!")