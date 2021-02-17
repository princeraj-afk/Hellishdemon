class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

def getLevelUtil(node, data, level):
    if (node == None):
        return 0

    if (node.data == data):
        return level

    downlevel = getLevelUtil(node.left,data, level + 1)
    if (downlevel != 0):
        return downlevel

    downlevel = getLevelUtil(node.right,data, level + 1)
    return downlevel

def getLevel(node, data):
    return getLevelUtil(node, data, 1)

for t in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    data = Node(a[0])
    for i in range(1,n):
        data.insert(a[i])
    for i in a:
        print(getLevel(data,i)-1,end=" ")
    print()