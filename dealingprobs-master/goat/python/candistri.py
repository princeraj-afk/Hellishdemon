a = int(input("Enter no of Total Candies\n"))
i=1
if a%2==0:
    while (i<a/2):
        print(a-i,i)
        i=i+1
elif a%2==1:
    while (i<a/2):
        print(a-i,i)
        i=i+1
print("No of ways:",a//2)