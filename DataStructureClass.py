# 链表
class LinkL():
    def __init__(self, data,link = None):
        self.data = data
        self.link = link

# 栈
class DStack():
    def __init__(self, maxSize = 999):
        self.__maxSize = maxSize
        self.slist = []

    def push(self, elem):
        if len(self.slist) >= self.__maxSize:
            return False
        self.slist.append(elem)
        return True

    def pop(self):
        if len(self.slist) == 0:
            return None
        return self.slist.pop(-1)

    def noEmp(self):
        if len(self.slist) == 0:
            return False
        return True

    def getTop(self):
        if len(self.slist) == 0:
            return None
        return self.slist[-1]

    def test(self):
        print(self.slist[0])

    def printStack(self):
        print(self.slist)

# 二叉树定义
class BitTree():
    def __init__(self, data = None, llink = None, rlink = None):
        self.llink = llink
        self.rlink = rlink
        self.data = data


# 带子节点数目的二叉树定义
class BitTreec():
    def __init__(self, data=None, llink=None, rlink=None, count = 0):
        self.llink = llink
        self.rlink = rlink
        self.data = data
        self.count = count

if __name__ == '__main__':
    stack = DStack()
    for i in range(10):
        stack.push(i)
    while stack.noEmp():
        print(stack.pop())
