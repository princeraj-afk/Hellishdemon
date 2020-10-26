class Calculator:
    def power(self,a,b):
        if a>=0 and b>=0:
            return a**b
        else:
            raise ValueError

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)