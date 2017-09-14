# 邻接矩阵图定义
class MGrapg():
    def __init__(self, n, type = 0):
        self.size = n
        self.l1 = []
        self.TYPE = type
        for i in range(0,n):
            l2 = list( 0 for i in range(0,n))
            self.l1.append(l2)

    # 插入顶点
    def insert_vertex(self,):
        self.size += 1
        for a in self.l1:
            a.append(0)
        temp = []
        self.l1.append(list( 0 for i in range(0,self.size)))


    def add_edge(self,v1, v2, weight = 1):
        if self.TYPE == 0:
            self.__add_edge0(v1, v2, weight)
        else:
            self.__add_edge0(v1, v2, weight)

    def __add_edge0(self,v1, v2 , weight = 1):
        self.l1[v1][v2] = weight
        self.l1[v2][v1] = weight

    def __add_edge1(self,v1, v2 , weight = 1):
        self.l1[v1][v2] = weight

    def remove_edge(self, v1, v2):
        if self.TYPE == 0:
            self.__remove_edge0(v1, v2)
        else:
            self.__remove_edge1(v1, v2)

    def __remove_edge0(self, v1, v2):
        self.l1[v1][v2] = 0
        self.l1[v2][v1] = 0

    def __remove_edge1(self, v1, v2):
        self.l1[v1][v2] = 0

    # 删除顶点
    def delete_vertex(self, vertex):
        self.size -= 1
        self.l1.pop(vertex)
        for a in self.l1:
            a.pop(vertex)

    def first_neighbor(self, v):
        for i in range(0, self.size):
            if self.l1[v][i] != 0:
                return i
        return -1

    def next_neighbor(self, v, x):
        if v+1 >= self.size:
            return -1
        for i in range(x+1, self.size):
            if self.l1[v][i] != 0:
                return i
        return -1

    def get_type(self):
        if self.TYPE == 0:
            print("无向图")
        else:
            print("有向图")

    def printMGrape(self):
        for a in self.l1:
            print(a)
        print("~~~~~~~~~~~~~~~~~~")

# 邻接表图定义
class BitTree():
    def __init__(self, data = None, llink = None, rlink = None):
        self.llink = llink
        self.rlink = rlink
        self.data = data

# 从前序和中序遍历获得一颗二叉树(任意数据)
def newBitTree4FM(flist, mlist):
    if flist == mlist == "":
        return None
    if flist == mlist and len(flist) == 1:
        return BitTree(flist)
    mid = mlist.index(flist[0])
    bit = BitTree(mlist[mid])
    bit.llink = newBitTree4FM(flist[1:mid+1], mlist[0:mid])
    bit.rlink = newBitTree4FM(flist[mid+1:len(flist)], mlist[mid+1:len(mlist)])
    return bit

# 随机的连接n个节点，使二叉树成为普通图
def randomLinkNode(g,n):
    pass

def BFSTraverse(g):
    l = []

if __name__ == '__main__':
    mg = MGrapg(5)
    mg.printMGrape()
    mg.add_edge(0, 1)
    mg.add_edge(1, 2)
    mg.add_edge(4, 3)
    mg.printMGrape()
    mg.insert_vertex()
    mg.add_edge(1, 4)
    mg.add_edge(1, 5)
    # mg.printMGrape()
    # mg.delete_vertex(1)
    # mg.printMGrape()
    nigeh = mg.first_neighbor(1)
    while (nigeh != -1):
        print(nigeh)
        nigeh = mg.next_neighbor(1,nigeh)
