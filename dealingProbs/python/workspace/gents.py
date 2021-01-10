def leap(a):
    if a % 4 == 0:
        if a % 400 == 0:
            return True
        elif a % 100 == 0 and a>1918:
            return False
        return True
    return False

n = int(input())
if n == 1918:
    print("26.09.1918")
elif leap(n) == True:
    print("12.09." + str(n))
else:
    print("13.09." + str(n))