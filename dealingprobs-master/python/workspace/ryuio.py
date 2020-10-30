
def ctrl(ans,table,key,n,s):

    if key==0 or key==n//2:
        return ans
    else:
        start = 0
        end = n
        for i in range(n):
            if s[i] != table[i]:
                start = i
                break
        for i in range(1, n + 1):
            if s[-i] != table[-i]:
                end = -i
                break
        s[start:end+1] = reversed(s[start:end+1])
        ans += 1
        key = s[::2].count("1")
        ctrl(ans,table,key,n,s)

for _ in range(int(input())):
    ans = 0
    n = int(input())
    s = list(input())
    key = s[::2].count("1")
    t1 = ["1", "0"] * (n // 2)
    t2 = ["0", "1"] * (n // 2)
    if key>=n/4:
        ans = ctrl(ans,t1,key,n,s)
    else:
        ans = ctrl(ans,t2,key,n,s)
    print(ans)