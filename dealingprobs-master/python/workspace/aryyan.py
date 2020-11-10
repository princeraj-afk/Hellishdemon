a = list(input())
ans = ""
if a[0]=="9":
    ans += "9"
    a.pop(0)
for i in a:
    if int(i)>4:
        ans += str(9 - int(i))
    else:
        ans+=i
print(int(ans))