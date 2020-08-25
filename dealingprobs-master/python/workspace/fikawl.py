import random
def rohandas_func(num):
    b = random.randint(1,10)
    wrong_num = random.randint(num*(b-.5),num*(b+.5))
    multi_table = []
    c=1
    while c<=10:
        multi_table.append(c*num)
        c = c+1
        continue
    multi_table[b-1] = wrong_num
    return multi_table
def actual_mult(num):
    multi_table=[]
    g=1
    while g<=10:
        multi_table.append(g * num)
        g= g + 1
        continue
    return multi_table

num = int(input("Enter the no whose u want to get ur multiplication table"))
list1 = rohandas_func(num)
print("Rohan das mutiplication table:\n",list1)
list2 = actual_mult(num)
print("Actual mutiplication table:\n",list2)

c =1
while(c<10):
    if list1[c] == list2[c]:
        c=c+1
        continue
    else:
        print(f"Rohan das is a fraud & he printed {num}*{c+1} as {list1[c]} where as it is {list2[c]}")
        c=c+1
        continue