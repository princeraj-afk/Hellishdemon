import time
from functools import lru_cache
n= int(input("How many data u wanna cache?\n"))
@lru_cache(maxsize= n)
def sqr(a):
    time.sleep (2)
    print (a*a)
if __name__ == '__main__':
    sqr(1)
    sqr(2)
    sqr(3)
    sqr(6)
    sqr(2)
    sqr(5)