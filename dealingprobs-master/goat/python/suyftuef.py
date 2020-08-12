a = int(input("enter no of students\n"))
list1 = []
dict1 = {}
for i in range(a):
    list1.append(input().split())
b = input()
for i in range(a):
    if b == list1[i][0]:
        print((int(list1[i][1])+int(list1[i][2])+int(list1[i][3]))/3)
    else:
        pass