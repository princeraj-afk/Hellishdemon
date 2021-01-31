import os
os.chdir("E:\ReactJS_Tutorial_for_Beginners")
t = set()
for i in os.listdir():
    t.add(int(i[:2]))
#
print(set(range(1,78)).difference(t))
# print(set(range(1,78)))
# print(t)