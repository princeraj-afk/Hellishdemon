import os
os.chdir("D:\jtest")

for i in os.listdir("D:\jtest"):
    os.rename(i,i[4:])