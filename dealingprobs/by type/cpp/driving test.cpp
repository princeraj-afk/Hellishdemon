print ("Enter your age")
a = int(input())
if a>7 and a<18 :
    print("Sorry, You cannot drive!")
elif a == 18:
    print("Maybe, We will think about you!")
elif a > 18 and a < 125:
    print("Congrats, You can drive!")
else:
    print("Please, Enter a valid age!")
