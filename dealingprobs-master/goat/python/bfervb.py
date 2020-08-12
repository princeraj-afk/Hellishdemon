import re
str1='''cjernkcje'''
list1 = re.findall(r'\w+@\S+\w',str1)

op=open("email_store.txt","a")

j=1
for i in list1:
    op.write(f"Email{j}:{i}\n")
    j=j+1
op.close()

print(f"Email's are:{list1}")
print(f"Total Email's are:{j-1}")