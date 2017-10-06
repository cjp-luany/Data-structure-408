import random
from DataStructureClass import DStack

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
    def insert_vertex(self):
        self.size += 1
        for a in self.l1:
            a.append(0)
        temp = []
        self.l1.append(list( 0 for i in range(0,self.size)))

    # 添加边 0为无向图添加模式，其他数字为有向图模式
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

    # 删除边
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

    # 获得第一个邻接节点，返回值为序号
    def first_neighbor(self, v):
        for i in range(0, self.size):
            if self.l1[v][i] != 0:
                return i
        return -1

    # 获得下一个邻接节点，返回值为序号
    def next_neighbor(self, v, x):
        if x+1 >= self.size:
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

    def printGrape(self):
        for a in self.l1:
            print(a)
        print("~~~~~~~~~~~~~~~~~~")


# 顶点类
class ArcNode():
    def __init__(self, data, firstarc = None):
        self.data = data
        self.firstarc = firstarc

# 邻接点类
class AdjNode():
    def __init__(self, data, nextarc = None):
        self.data = data
        self.nextarc = nextarc

# 邻接表图定义
class ALGraph():
    def __init__(self, n, type = 0):
        self.size = n
        self.TYPE = type
        self.l1 = []
        for i in range(0,n):
            self.l1.append(ArcNode(i))

    # 插入顶点
    def insert_vertex(self):
        self.size += 1
        self.l1.append(ArcNode(self.size-1))

    # 获得第一个邻接节点
    def first_neighbor(self, v):
        if self.l1[v].firstarc != None: # firstarc不为空就返回firstarc
            return self.l1[v].firstarc.data
        return -1 # 否则返回-1

    # 获得下一个邻接节点
    def next_neighbor(self, v, x):
        temp  = self.l1[v].firstarc # 工作指针
        while (temp.nextarc != None): # 工作指针的下一个不为空就继续循环
            if temp.data == x: # 如果工作指针的值等于需要获得下一个节点的值
                return temp.nextarc.data # 返回下一个节点
            temp = temp.nextarc # 工作指针滚动
        return -1 # 没有下一个节点返回-1

    def delete_vertex(self, vertex):
        self.size -= 1
        for a in self.l1:
            self.remove_edge(a.data,vertex)# 调用删除边方法删除其他顶点里的对应边
        self.l1.pop(vertex) # 删除这个顶点对应的邻接链表

    # 添加边 0为无向图添加模式，其他数字为有向图模式
    def add_edge(self,v1, v2):
        if self.TYPE == 0:
            self.__add_edge0(v1, v2)
        else:
            self.__add_edge1(v1, v2)

    def __add_edge0(self,v1, v2 ):# 无向图加边等于有向图连一次，交换次序再连一次
        self.__add_edge1(v1, v2)
        self.__add_edge1(v2, v1)

    def __add_edge1(self,v1, v2):
        temp = self.l1[v1].firstarc
        if temp == None:
            self.l1[v1].firstarc = AdjNode(v2) # 只有顶点节点则直接添加邻接节点
            return
        while (temp.nextarc != None):# 循环到邻接链表尾部
            temp = temp.nextarc
        temp.nextarc = AdjNode(v2)


    # 删除边
    def remove_edge(self, v1, v2):
        if self.TYPE == 0:
            self.__remove_edge0(v1, v2)
        else:
            self.__remove_edge1(v1, v2)

    def __remove_edge0(self, v1, v2):
        self.__remove_edge1(v1, v2)
        self.__remove_edge1(v2, v1)

    def __remove_edge1(self, v1, v2):
        temp = self.l1[v1].firstarc
        if temp == None: # 遍历时若有无邻边的顶点则直接返回
            return
        if temp.data == v2: # 若是第一个邻接节点
            self.l1[v1].firstarc = temp.nextarc
            temp.nextarc == None

        while (temp != None and temp.nextarc != None): # 循环到邻接链表尾部,由于是比较下一个元素的值，到倒数第二个即可
            if temp.nextarc.data == v2: # 如果当前节点的下一个节点匹配
                temp2 = temp.nextarc
                temp.nextarc = temp2.nextarc
                temp2.nextarc = None
                temp2 = None
            temp = temp.nextarc

    def get_type(self):
        if self.TYPE == 0:
            print("无向图")
        else:
            print("有向图")

    def printGrape(self):
        for a in self.l1:
            tstr = ""
            tstr += str(a.data)
            temp = a.firstarc
            while (temp != None):
                tstr+=  "→" +str(temp.data)
                temp = temp.nextarc
            print(tstr)
        print("~~~~~~~~~~~~~~~~~~")

temp = []
queue = []
def BFSTraverse(g):
    global temp, queue
    for i in range(0,g.size):
        temp.append(False)
    # InitQueue(g)
    for i in range(0,g.size):
        if temp[i] == False:
            BFS(g, i)

def BFS(g, i):
    global temp, queue
    temp[i] = True
    print(i)
    queue.append(i)
    while (len(queue) != 0):
        i = queue.pop(0)
        w = g.first_neighbor(i)
        while (w >0 ):
            if temp[w] == False:
                print(w)
                temp[w] = True
                queue.append(w)
            w = g.next_neighbor(i,w)

def DFSTraverse(g):
    global temp, queue
    for i in range(0, g.size):
        temp.append(False)
    for i in range(0,g.size):
        if temp[i] == False:
            DFS(g, i)

def DFS(g, i):
    print(i)
    temp[i] = True
    w = g.first_neighbor(i)
    while (w > 0):
        if temp[i] == False:
            DFS(g, w)
        w = g.next_neighbor(i, w)

# 判断是否为树
def isTree(g):
    temp = []
    for i in range(0, g.size):
        temp.append(False)
    i = 0
    j = 0
    i,j = DFS_tree(g, 0, i, j, temp)
    print(i,j)
    if i == g.size and i*2-2 == j:
        return True
    else:
        return False

# 判断是否为树——递归主体
def DFS_tree(g, n, i, j, temp):
    temp[n] = True
    w = g.first_neighbor(n)
    i += 1
    while w!= -1:
        j += 1
        if temp[w] == False:
            i,j = DFS_tree(g, w, i, j, temp)
        w = g.next_neighbor(n, w)
    return i,j

# 无递归DFS
def DFS__stack(g):
    temp = []
    for i in range(0, g.size):
        temp.append(False)
    # InitStack(s)
    s = DStack()
    for i in range(0,g.size):
        if temp[i] == False:
            s.push(i)
            w = g.first_neighbor(i)
            while w != -1:
                if temp[w] == False:
                    s.push(w)
                    temp[w] = True
                w = g.next_neighbor(i, w)
    while s.noEmp():
        print(s.pop())

def DFS__stack2(g):
    temp = []
    for i in range(0, g.size):
        temp.append(False)
    # InitStack(s)
    s = DStack()
    for i in range(0,g.size):
        if temp[i] == False:
            s.push(i)
            temp[i] = True
            while s.noEmp(): # 栈不为空
                t = s.pop()
                print(t)
                w = g.first_neighbor(i)
                while w != -1:
                    if temp[w] == False:
                        s.push(w)
                        temp[w] = True
                    w = g.next_neighbor(i, w)

def have_neighbor_DFS(g,v1,v2):
    temp = []
    # InitQueue(q)
    q = []
    for i in range(0,g.size):
        temp.append(False)
    q.append(v1)
    temp[v1] = True
    while (len(q) != 0):
        t = q.pop(0)
        w= g.first_neighbor(t)
        if t == v2:
            return True
        while(w != -1):
            if temp[w] == False:
                q.append(w)
                print(w)
                temp[w] = True
            w = g.next_neighbor(t,w)
    return False



if __name__ == '__main__':
    # mg = MGrapg(5)
    # mg.printGrape()
    # mg.add_edge(0, 1)
    # mg.add_edge(1, 2)
    # mg.add_edge(4, 3)
    # mg.printGrape()
    # mg.insert_vertex()
    # mg.add_edge(1, 4)
    # mg.add_edge(1, 5)
    # mg.printGrape()
    # mg.delete_vertex(1)
    # mg.printGrape()
    # nigeh = mg.first_neighbor(1)
    # while (nigeh != -1):
    #     print(nigeh)
    #     nigeh = mg.next_neighbor(1,nigeh)

    # alg = ALGraph(5)
    # alg.printGrape()
    # alg.add_edge(0, 1)
    # alg.add_edge(1, 2)
    # alg.add_edge(4, 3)
    # alg.printGrape()
    # alg.insert_vertex()
    # alg.printGrape()
    # alg.add_edge(1, 4)
    # alg.add_edge(1, 5)
    # alg.printGrape()
    # alg.delete_vertex(4)
    # alg.printGrape()
    # nigeh = alg.first_neighbor(1)
    # while (nigeh != -1):
    #     print(nigeh)
    #     nigeh = alg.next_neighbor(1,nigeh)
    g = ALGraph(7,1)
    # g = ALGraph(7)
    l = [[0,6],[1,6],[1,4],[2,4],[2,5],[0,5],[6,4],]
    l2 = [[1,4],[1,5],[2,1],[3,2],[3,5],[4,2],[5,0],[5,6],[6,4]]
    for a in l:
        g.add_edge(a[0], a[1])
    # mg.printGrape()
    # mg = MGrapg(3)
    # mg.add_edge(0,1)
    # mg.add_edge(0, 2)
    # mg.add_edge(2, 1)
    # BFSTraverse(g)
    # DFSTraverse(g)
    # g2 = MGrapg(7) # 树
    # g = ALGraph(7)
    # l = [[0,6],[1,6],[6,4],[5,3],[2,5],[0,5]]
    # for a in l:
    #     g2.add_edge(a[0], a[1])
    # g2.printGrape()
    # BFSTraverse(g2)
    # DFSTraverse(g)
    # print("````````````")
    # print(isTree(g))
    # print(isTree(g2))
    # DFS__stack(g)
    # print("````````````")
    # DFS__stack2(g)
    # g.printGrape()
