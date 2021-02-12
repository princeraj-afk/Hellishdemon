a = int(input())
arr1 = [int(x) for x in input().split()]
arr2 = sorted(arr1)
diff = list(filter(lambda x:arr1[x]!=arr2[x],range(a)))

if len(diff)==0:
    print("yes\n1 1")
    exit()
if diff[-1]-diff[0]>len(diff):
    print("no")
    exit()
for i in range(len(diff)//2):
    arr1[diff[i]],arr1[diff[-(i+1)]] = arr1[diff[-(i+1)]],arr1[diff[i]]
print("yes\n"+""+str(diff[0]+1),diff[-1]+1) if arr1==arr2 else print("no")
