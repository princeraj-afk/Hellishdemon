#client name
print("Enter the diet u had now")
f=input()
print("Enter the exercise u did")
e=input()
def getdate():
    import datetime
    return datetime.datetime.now()
b=int(input("enter 1 for Brij Mohan\n 2 for Rekha Devi\n 3 for Prince Raj\n and 4 for Aryan Raj\n"))
print("\n\n\n")
print(getdate())
print("Client name:", end="")
if b==1:
    print("Brij Mohan")
elif b==2:
    print("Rekha Devi")
elif b==3:
    print("Prince Raj")
elif b==4:
    print("Aryan Raj")
else:
    print("Please enter whole no between 1 to 4")
print("Meal taken:", f)
print("Exercise done:", e)