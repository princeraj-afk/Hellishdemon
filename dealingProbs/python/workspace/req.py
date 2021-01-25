import os

os.chdir("E:\egotiable\chernobyl")

for i in os.listdir():
    episode = i[:-3]
    format = i[-3:]
    os.rename(i,episode+"."+format.lower())