import re
a = input()
a = list(a)
vowels = ('a','e','i','o','u','A','E','I','O','U')
consonants = ('b','c','d','f','g','h','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','Q','W','R','T','Y','P','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M')
count = 0
for i in range(len(a)):
    if a[i] in vowels:
        count +=1
        if count>=2:
            print(a[i],end="")
        continue
        print("\n")
    else:
        count=0
        pass