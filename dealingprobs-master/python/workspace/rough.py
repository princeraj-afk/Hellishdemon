import numpy as np
class HashTable:
    def __init__(self):
        self.max = 100
        self.arr  = [[] for _ in range(self.max)]
    def get_hash(self,key):
        h = 0
        return sum(ord(char) for char in key)

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            self.arr[h].append((key,value))

    def __getitem__(self, item):
        h = self.get_hash(item)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None


if __name__ == '__main__':
    t = HashTable()
