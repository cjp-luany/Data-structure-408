import random

from DataStructureClass import LinkL

# 创建链表
def newRandomLink(n):
    node = None
    for i in range(n):
        node = LinkL(random.randint(0,n), node)
        i+=1
    node = LinkL("头结点", node)
    return node

def newLink(n):
    node = None
    for i in range(n):
        node = LinkL(n-i,node)
        i+=1
    node = LinkL("头结点", node)
    return node

# 释放节点（伪）
def freeNode(node):
    print("节点%s已删除"%node.data)

# 输出链表
def printLink(l):
    print("准备输出")
    s = ""
    while(l.link != None):
        l = l.link
        s=s + str(l.data)+" "
    print(s)

# 按值删除
def delLink (l,x):
    pNode = None
    while (l.link != None):
        if l.link.data == x:
            pNode = l.link
            l.link = l.link.link
            freeNode(pNode)
        l = l.link

def re1 (l):
    # 空链表或单元素链表直接返回
    if l.link==None or l.link.link==None :
        return l
    # 第一个节点
    p1 = l.link
    # 第二个节点
    p2 = p1.link
    # 反转完成的部分
    p3 = None
    while p2.link != None:
        p1.link = p3
        p3 = p1
        p1 = p2
        p2 = p2.link
    # 倒数第二节点指向已反序列
    p1.link = p3
    # 倒数第一节点指向倒数第二节点
    p2.link = p1
    l.link = p2

def re2 (l):
    p1 = None
    p2 = None
    p1 = l.link
    l.link = None
    while p1 != None:
        p2 = p1.link
        p1.link = l.link
        l.link = p1
        p1 = p2

def sortLink(l):
    old = l
    p1 = old.link
    old.link =None
    while p1!= None:
        p2 = p1.link
        old = l
        while old!= None and old.link != None and old.link.data < p1.data:
            old = old.link
        p1.link = old.link
        old.link = p1
        p1 = p2

def reSort(l1,l2):
    p1 = None
    p2 = None
    r = None
    p1 = l1.link
    p2 = l2.link
    l1.link = None
    l2.link = None
    while p1 != None and p2 != None:
        if p1.data < p2.data:
            r = p1
            p1 = p1.link
        else:
            r = p2
            p2 = p2.link
        r.link = l1.link
        l1.link = r
    if p1 == None:
        while p2 != None:
            r = p2
            p2= p2.link
            r.link = l1.link
            l1.link = r
    if p2 == None:
        while p1 != None:
            r = p1
            p1 = p1.link
            r.link = l1.link
            l1.link = r

def exc(l1,l2):
    p1 =None
    p2 = None
    s = None
    r = None
    p1 = l1.link
    p2 = l2.link
    l1.link = None
    s = l1
    freeNode(l2)
    l2.link = None
    while p1 != None and p2 != None:
        if p1.data == p2.data:
            s.link = p1
            s = p1
            p1 = p1.link
            r = p2
            p2 = p2.link
            freeNode(r)
            s.link = None
        elif p1.data < p2.data:
            r = p1
            p1 = p1.link
            freeNode(r)
            r.link == None
        else:
            r = p2
            p2 = p2.link
            freeNode(r)
            r.link == None

    while p1 != None:
        s = p1
        p1 = p1.link
        freeNode(s)

    while p2 != None:
        s = p2
        p2 = p2.link
        freeNode(s)

def son(l1,l2):
    p1 = None
    p2 = None
    p1 = l1.link
    p2 = l2.link
    while p1 != None and p2 != None:
        if p1.data == p2.data:
            p2 = p2.link
        else:
            p2 = l2.link
        p1 = p1.link
    if p2 == None:
        print("true")
    else:
        print("false")

def refind(l,n):
    p1 = None
    p2 =None
    p1 = l.link
    p2 = l.link
    while n > 0 and p2 != None:
        p2 = p2.link
        n-=1
    if p2 == None:
        print(0)
        return
    while p2 != None:
        p1 = p1.link
        p2 = p2.link
    print(p1.data)
    print(1)

if __name__ == '__main__':
    '''(按值删除测试)
    LinkList = newLink(10)
    printLink(LinkList)
    delLink(LinkList,10)
    printLink(LinkList)
    '''

    ''' 反序
    LinkList = newLink(10)
    printLink(LinkList)
    re1(LinkList)
    # re2(LinkList)
    printLink(LinkList)
    '''

    ''' 排序
    LinkList = newRandomLink(10)
    printLink(LinkList)
    sortLink(LinkList)
    printLink(LinkList)
    '''
    '''链表反续归并
    LinkList1 = newLink(10)
    LinkList2 = newLink(10)
    printLink(LinkList1)
    reSort(LinkList1,LinkList2)
    printLink(LinkList1)
    '''

    '''有序链表并集
    l1 = newRandomLink(10)
    l2 = newRandomLink(10)
    sortLink(l1)
    sortLink(l2)
    printLink(l1)
    printLink(l2)
    exc(l1,l2)
    printLink(l1)
    '''
    '''
    l1 = newLink(20)
    l2 = newLink(10)
    son(l1,l2)
    delLink(l1, 9)
    son(l1, l2)
    delLink(l2, 9)
    delLink(l2, 1)
    son(l1, l2)
    '''

    l1 = newLink(10)
    printLink(l1)
    refind(l1,15)