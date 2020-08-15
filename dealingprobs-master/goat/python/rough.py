class Treenode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent =None

    def addchild(self,child):
        child.parent = self
        self.children.append(child)


if __name__ == '__main__':
