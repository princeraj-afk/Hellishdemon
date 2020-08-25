a = int(input("Enter the no of elements u wanna print"))
char = input("enter words using space between them")
list1 = char.split(" ")
type = int(input("WHich type of comprehension u wanna use\n 1.set\n2.list\n3.dict"))
if type==1:
    s= {j for j in list1}
    print(s)
    print(type(s))
