import random

from DataStructureClass import DStack,BitTree,BitTreec



# 按序生成一颗二叉树
def newBitTree():
    b = BitTree(0)
    l = []
    l.append(b)
    i = 1
    while (i<10):
        t = l.pop()
        left = BitTree(i)
        i+=1
        right = BitTree(i)
        i+=1
        t.llink = left
        t.rlink = right
        l.insert(0,left)
        l.insert(0,right)
    return b

# 递归后序遍历
def postOeder(t):
    if t != None:
        postOeder(t.llink)
        postOeder(t.rlink)
        print(t.data)

# 非递归后续遍历
def noStackPostOrder(t):
    stack = DStack()
    flag = None
    while t!= None or stack.noEmp():
        if t!= None:
            stack.push(t)
            t = t.llink
        else:
            t = stack.getTop()
            if t.rlink != None and t.rlink != flag:
                t = t.rlink
                stack.push(t)
                t = t.llink
            else:
                t = stack.pop()
                print(t.data)
                flag = t
                t = None

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

# 从前序和中序遍历获得一颗二叉树（数字数据）
def newBitTree4FM2(flist, mlist, f1, f2, m1, m2):
    bit = BitTree(int(flist[f1]))
    mid = m1
    while mlist[mid] != flist[f1]:
        mid += 1
    llen = mid - m1
    rlen = m2 - mid
    if llen!= 0:
        bit.llink = newBitTree4FM2(flist,mlist,f1+1, f1+llen, m1, m1+llen-1)
    else:
        bit.llink = None
    if rlen != 0:
        bit.rlink = newBitTree4FM2(flist, mlist, f2-rlen+1, f2, m2 - rlen+1, m2)
    else:
        bit.rlink = None
    return  bit

# 删除二叉树（python没有free函数故这只是个架子）
def delTree(t):
    if t == None:
        return True
    delTree(t.llink)
    delTree(t.rlink)
    return True


# 查找指定值的节点
def findTree(t,e):
    flag = False
    if t == None:
        return
    if t.data == e:
        flag = delTree(t)
    if flag:
        print(t.data) # 没有free方法，故只在这里检测是否成功找到所需节点并中止本次循环
        return
    findTree(t.llink,e)
    findTree(t.rlink,e)

# 打印公共父节点路径
def findPars(t, e):
    flag1 = False
    flag2 = False
    if t == None:
        return False
    if t.data == e:
        return True
    flag1 = findPars(t.llink, e)
    flag2 = findPars(t.rlink, e)
    if flag1 or flag2:
        print(t.data)
        return True
    else:
        return False

# 查找第一个公共父节点
def findDuPar(t, e1, e2):
    flag1 = False
    flag2 = False
    if t == None:
        return False
    if t.data == e1 or t.data == e2:# 实际是直接比较即可
        return True
    flag1 = findDuPar(t.llink, e1, e2)
    flag2 = findDuPar(t.rlink, e1, e2)
    if flag2 and flag1:
        print(t.data) # 实际是返回给外部变量
        return False # C语言中有exit(0)，可以直接退出
    if flag2 or flag1:
        return True
    else:
        return False

# 获取最大宽度
def getMaxWidth(t):
    i = 1
    j = 0
    q = [] # 模拟队列
    q.append(t)
    max_width = 0 # 实际中需要提前声明的最大值变量
    while len(q) != 0:
        if i > max_width:
            max_width = i
        while (i > 0):
            t = q.pop(0)
            i -= 1
            if t.llink != None:
                q.append(t.llink)
                j += 1
            if t.rlink != None:
                q.append(t.rlink)
                j += 1
        i = j
        j = 0
    print(max_width)

# 从满二叉树的前序序列得后续序列
def pre2Post(pre, l1, h1, post, l2, h2):
    print(l1, h1, l2, h2)
    half = 0
    if h1 >= l1:
        half = int((h1 - l1) / 2)
        post[h2] = pre[l1]
        print(half)
        print(post)
        pre2Post(pre, l1 + 1, l1 + half, post, l2, l2 + half - 1)
        pre2Post(pre, l1 + half + 1, h1, post, l2 + half, h2 - 1)

# 各叶节点的权值路径之和
def sum_weight(b, i):
    w1 = 0 # int w1= 0
    w2 = 0 # int w2 = 0
    i += 1
    if b == None:
        return 0
    if b.llink == None and b.rlink == None:
        return i * b.data
    w1 = sum_weight(b.llink, i)
    w2 = sum_weight(b.rlink, i)
    return w1 + w2

# 返回二叉树的深度
def h1(b):
    if b == None:
        return 0
    hl = h1(b.llink)
    hr = h1(b.rlink)
    if (hl+1 > hr):
        return hl+1
    else:
        return hr

# 参数：层序、度、终止位置
def newCBTree(data, degree, n):
    nodes = []
    d = 0
    k = 0
    for i in range(0,n):
        nodes.append(BitTree(data[i]))
    for i in range(0,n):
        d = degree[i]
        if (d):
            k+=1
            nodes[i].llink = nodes[k]
            for j in range(2,d+1):
                nodes[k].rlink = nodes[k+1]
                k+=1
    return nodes[0]

# 判断指定的二叉树是否为BST树
temp = -11037
def isBSTTree(t):
    global temp
    if t == None:
        return 1
    b1 = isBSTTree(t.llink)
    if b1 == 0 or temp >= t.data:
        return 0
    temp = t.data
    b2 = isBSTTree(t.rlink)
    return b2

# 判断指定的节点在树中的层次
def getNodeinTree(b,e):
    queue = []
    queue.append(b)
    c = 1 # 层数
    i = 1 # 当前层在队列中的节点数
    j = 0 # 当前层的子节点在队列中的个数
    while b != None:
        t = queue.pop(0)
        i -= 1
        if t == e:
            return c
        if t.llink != None:
            queue.append(t.llink)
            j += 1
        if t.rlink != None:
            queue.append(t.rlink)
            j += 1
        if i == 0:
            i = j
            j = 0
            c += 1

# 判断指定的节点在BST树中的层次
def getNodeinBSTTree(b,e):
    c = 0
    if  b != None:
        c += 1
        while b != e:
            if b.data < e.data:
                b = b.rlink
            else:
                b = b.llink
            c += 1
    return c

# 判断一棵树是否为AVL树
def isAVLTree(b):
    if b == None:
        return 0
    if b.llink == None and b.rlink == None:
        return 1
    b1 = isAVLTree(b.llink)
    b2 = isAVLTree(b.rlink)
    if b1 == -1 or b2 == -1:
        return -1
    if abs(b1-b2)>1:
        return -1
    return max(b1,b2)+1

minNode = None
maxNode = None
# 获取排序二叉树中最小和最大节点的值1
def getMinMax4BSTTree(b):
    global minNode
    global maxNode
    if b == None:
        return None
    getMinMax4BSTTree(b.llink)
    if minNode == None or b.data < minNode:
        minNode = b.data
    if maxNode == None or b.data > maxNode:
        maxNode = b.data
    getMinMax4BSTTree(b.rlink)

# 获取排序二叉树中最小和最大节点的值1
def getMinMax4BSTTree2(b):
    minNode = b
    maxNode = b
    while(minNode.llink != None):
        minNode = minNode.llink
    while(maxNode.rlink != None):
        maxNode = maxNode.rlink
    print(minNode.data,maxNode.data)

# 降序打印二叉排序树中大于等于key值的节点值
def printBSTTree(b,key):
    if b == None:
        return  None
    printBSTTree(b.rlink,key)
    if b.data>= key:
        print(b.data)
    printBSTTree(b.llink,key)

nodetim = None
# 获取排序二叉树中第n小的元素
def getindexNode4BSTTree(b,n):
    global nodetim

    if b.llink == None:
        if n == 1:
            nodetim = b
            return
        else:
            getindexNode4BSTTree(b.rlink, n - 1)

    if n == b.count - b.rlink.count:
        nodetim = b
    if n>b.llink.count+1:
        getindexNode4BSTTree(b.rlink, n-1-b.llink.count)
    if n<b.llink.count+1:
        getindexNode4BSTTree(b.llink, n)

# 获取排序二叉树中第n小的元素2
def getindexNode4BSTTree2(b,n):
    if n<1 or n>b.count:
        return None
    if b.llink == None:
        if n == 1:
            return b
        else:
            return getindexNode4BSTTree2(b.rlink, n-1)
    else:
        if b.llink.count == n-1:
            return b
        if b.llink.count > n-1:
            return getindexNode4BSTTree2(b.llink,n)
        if b.llink.count < n-1:
            return getindexNode4BSTTree2(b.rlink,n-b.llink.count-1)

# 递归获得节点层数和data
def getData_cen(b,c):
    if b == None:
        return
    c += 1
    getData_cen(b.llink,c)
    print(b.data,c)
    getData_cen(b.rlink,c)

if __name__ == '__main__':
    # bittree = newBitTree()
    # PostOeder(bittree)
    # print("++++++++++++++")
    # PostOeder(bittree)
    s1 = "641235879"
    s2 = "123456789"
    # s1 = 'a'
    # s2 = 'a'
    # bit = newBitTree4FM(s1,s2)
    bit = newBitTree4FM2(s1, s2 , 0 ,len(s1)-1, 0, len(s2)-1)
    # bit.llink.llink.data = 1
    # bit.llink.rlink.llink.data = 2
    # bit.llink.rlink.rlink.data = 3
    # bit.rlink.llink.data = 4
    # bit.rlink.rlink.rlink.data = 5
    # print(bit.data)
    # print(bit.rlink.data)
    # print(bit.rlink.rlink.data)
    # print(bit.rlink.llink.llink.data)
    # findTree(bit,"b")
    # print(bit.rlink.llink.data)
    # findPars(bit,"b")
    # findDuPar(bit,"h","f")
    # findDuPar(bit, "e", "l")
    # getMaxWidth(bit)
    # s3 = ["a","b","d","e","c","f","g"]
    # s4 = ["@","@","@","@","@","@","@"]
    # Pre2Post(s3,0,6,s4,0,6)
    # print(s4)
    # print(int(1/2))
    # print(sum_weight(bit, 0))
    # print(h1(bit))
    # s3 = ["a","b","c","d","e","f","g","h","i"]
    # s4 = [3,3,0,2,0,0,0,0,0]
    # b = NewCBTree(s3,s4,len(s3))
    # print(b.llink.data)
    # print(b.llink.llink.data)
    # print(b.llink.rlink.data)
    # print(isBSTTree(bit))
    e1 = bit.llink.rlink # 3
    e3 = bit.rlink.rlink # 3
    # print(getNodeinTree(bit, e1))
    # print(getNodeinTree(bit, e2))
    # print(getNodeinTree(bit, e3))
    # print(getNodeinBSTTree(bit, e1))
    # print(getNodeinBSTTree(bit, e3))
    # print(isAVLTree(bit))
    # getMinMax4BSTTree(bit)
    # print(minNode,maxNode)
    # getMinMax4BSTTree2(bit)
    # printBSTTree(bit,5)

    # 对带子节点数目的二叉树的各节点添加子节点数目，需要BitTreec这个特殊的二叉树类才能运行
    def NodeCount(b):
        if b == None:
            return 0
        b1 = NodeCount(b.llink)
        b2 = NodeCount(b.rlink)
        b.count = b1+b2+1
        return b.count
    NodeCount(bit)
    # print(bit.llink.rlink.count)
    # getindexNode4BSTTree(bit, 5)
    # nodetim = getindexNode4BSTTree2(bit, 5)
    # print(nodetim.data)
    # getData_cen(bit,0)
    noStackPostOrder(bit)