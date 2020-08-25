n = int(input("Enter the length of list\n"))
list1 = []
for i in range(n):
    value = input("Enter the list items\n")
    list1.append(value)
list2 = list1.copy()
list2.reverse()
list3 =list1[::-1]
if n%2 == 1:
    c = 0
    b = 0
    for value in list1:
        while(c<n/2):
            b = list1[n-c-1]
            list1[n-c-1] = list1[c]
            list1[c] = b
            c = c+1
        continue
else:
    c=0
    b=0
    for items in list1:
        while(c<n/2):
            b=list1[n - c - 1]
            list1[n - c - 1]=list1[c]
            list1[c]=b
            c=c + 1
        continue
if list1 == list2 and list2 == list3:
    print(list1)
else:
    print("Error shown!")