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
            self.__add_edge0(v1, v2)

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
        if temp == None:# 遍历时若有无邻边的顶点则直接返回
            return
        if temp.data == v2:# 若是第一个邻接节点
            self.l1[v1].firstarc = temp.nextarc
            temp.nextarc == None

        while (temp != None and temp.nextarc != None):# 循环到邻接链表尾部,由于是比较下一个元素的值，到倒数第二个即可
            if temp.nextarc.data == v2:# 如果当前节点的下一个节点匹配
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

    alg = ALGraph(5)
    alg.printGrape()
    alg.add_edge(0, 1)
    alg.add_edge(1, 2)
    alg.add_edge(4, 3)
    alg.printGrape()
    alg.insert_vertex()
    alg.printGrape()
    alg.add_edge(1, 4)
    alg.add_edge(1, 5)
    alg.printGrape()
    alg.delete_vertex(4)
    alg.printGrape()
    nigeh = alg.first_neighbor(1)
    while (nigeh != -1):
        print(nigeh)
        nigeh = alg.next_neighbor(1,nigeh)