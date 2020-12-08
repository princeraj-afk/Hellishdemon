a = int(input("Enter either your age or year of birth\n"))
b = 2020
while True:
    if a<= 150  and a > 0:
        yob = 2020-a
        break
    elif a >= 1870 and a <= 2020:
        yob = a
        break
    elif a <= 0:
        print("You are not yet born!")
        break
    else:
        print("Enter a valid age or year of birth!")
        a=int (input ("Enter either your age or year of birth\n"))
        continue

if yob >= 1895:
    print("you will turn 100 year old in:",(yob+100))
elif yob>1870 and yob<=1895:
    print("You seem to be one of the oldest person alive!\nYou will turn 100 year old in:",(yob+100))

while True:
    print("Enter 0 to quit and 1 to continue")
    z = int(input())
    if z==1:
        print("Enter the year u wanna know your age!")
        s = int(input())
        if s>yob:
            print(f"You will be {s-yob} year old in {s}")
        else:
            print("Don't enter an year when you were not born!")
    elif z==0:
        break
    else:
        continue