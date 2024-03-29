import random


# 定义一个节点
class Node:
    # 初始化节点的值
    def __init__(self, data):
        self.data = data
        self.next = None

    # 获得节点的值
    def getData(self):
        return self.data

    # 获得下个节点的指针
    def getNext(self):
        return self.next

    # 设置节点的值
    def setData(self, newData):
        self.data = newData

    # 设置下一个节点
    def setNext(self, nextNode):
        self.next = nextNode


# 单链表
class SingleLinkedList:
    def __init__(self):
        self.head = Node(None)

    def printData(self):  # 打印链表的方法
        current = self.head
        l = []
        while current.getNext():
            number = current.getData()
            if number is not None:
                l.append(number)
            current = current.getNext()
        return l

    # 尾插法建表
    def weiChaFa(self):
        # 这里用一个列表来记录每次随机生成的数字，方便对比
        l = []
        r = self.head  # 游标，指定链表的头部
        for i in range(10):
            data = random.randint(0, 100)  # 随机生成一个1~100的数字
            l.append(data)
            s = Node(data)  # 新建一个新节点
            r.setNext(s)  # 头部的指针指向这个新节点
            r = s  # 游标指向最后的新节点
        print("插入的随机生成数字为:\t", *l)
        print("尾插法生成的单链表数字为:\t", *self.printData())

    # 头插法建表
    def touChaFa(self):
        # 这里用一个列表来记录每次随机生成的数字，方便对比
        l = []
        for i in range(10):
            data = random.randint(0, 100)  # 随机生成一个1~100的数字
            l.append(data)
            temp = Node(data)  # 建造一个节点，并初始值为data
            temp.setNext(self.head)  # 节点指针指向头指针
            self.head = temp
        print("插入的随机生成数字为:\t", *l)
        print("头插法生成的单链表数字为:\t", *self.printData())

    # 判断链表是否为空
    def isEmpty(self):
        return self.head == None

    # 判断链表长度
    def size(self):
        length = 0
        current = self.head
        while current != None:
            length += 1
            current = current.getNext()
        return length

    # 删除链表中的元素
    def remove(self, data):
        current = self.head  # 当前的节点
        previous = None  # 上一个节点
        found = False
        while not found and current:  # 找到就打上发现的标签
            if current.getData() == data:
                found = True
            else:  # 没找到就顺着指针往下找
                previous = current
                current = current.getNext()
        if current is None:  # 链表中不存在这个元素
            return False
        if previous == None:  # 当删除的元素为第一个元素时
            self.head = current.getNext()
        else:  # 当删除的元素不是在第一个元素时
            previous.setNext(current.getNext())
        return True

    # 查找链表中的元素,发现则返回下标的位置，否则返回-1
    def search(self, data):
        count = -1
        current = self.head.getNext()
        while current is not None:
            count += 1
            if current.getData() == data:
                return count
            else:
                current = current.getNext()
        return -1


L1, L2 = SingleLinkedList(), SingleLinkedList()
L1.weiChaFa()
L2.touChaFa()
print(L1.search(1))
print(L1.remove(1))
