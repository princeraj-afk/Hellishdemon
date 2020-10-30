for i in range(int(input())):
    n,k = map(int,input().split());x,y = n-(k-1),n-2*(k-1)
    if x%2!=0 and x>0:print('YES');print('1 '*(k-1)+str(x))
    elif y%2==0 and y>0:print('YES');print('2 '*(k-1)+str(y))
    else:print('NO')