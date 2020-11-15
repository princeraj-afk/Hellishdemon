import requests
from itertools import chain
from tqdm import tqdm

g = open("patch.txt","w")
counter = 0
p = list(chain(range(48,58), range(65,91),range(97,123)))

while(counter<5):
    for a in p:
        for b in p:
            for c in p:
                for d in p:
                    for e in p:
                         for f in p:
                            s="https://gpay.app.goo.gl/"+chr(a)+chr(b)+chr(c)+chr(d)+chr(e)+chr(f)
                            r = requests.get(s)
                            if str(r) == "<Response [200]>":
                                g.write(s+"\n")
                                counter+=1
