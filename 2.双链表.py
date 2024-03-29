import random


class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

        # 获得节点的值

    def getData(self):
        return self.data

    # 获得下个节点的指针
    def getNext(self):
        return self.next

    def getPrevious(self):
        return self.previous

    # 设置节点的值
    def setData(self, newData):
        self.data = newData

        # 设置下一个节点

    def setPrevious(self, previousNode):
        self.previous = previousNode

    def setNext(self, nextNode):
        self.next = nextNode


class DoubleLinkList:
    def __init__(self):
        self.head = Node(None)

    def printData(self):  # 打印链表的方法
        current = self.head.next
        l = []
        while current.getData() != None:
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
            data = random.randint(0, 10)  # 随机生成一个1~100的数字
            l.append(data)
            s = Node(data)  # 新建一个新节点
            r.setNext(s)  # 头部的指针指向这个新节点
            s.setPrevious(r)  # 节点的指针指向上一个节点
            r = s  # 游标指向最后的新节点
        r.setNext(self.head)  # 将最后一个节点的后继指针指向链表的头部，构成循环
        print("插入的随机生成数字为:\t", *l)
        print("尾插法生成的单链表数字为:\t", *self.printData())

    def search(self, data):
        current = self.head.next
        found = False
        while current.getData() != None and not found:
            if current.getData() == data:
                found = True
                break
            else:
                current = current.getNext()
        return found

    def remove(self, data):
        current = self.head.next
        found = False
        while current.getData() != None and not found:
            if current.getData() == data:
                found = True
                pre = current.getPrevious()
                next = current.getNext()
                next.setPrevious(pre)
                if pre != None:
                    pre.setNext(next)
                break
            else:
                current = current.getNext()
        return found


doubleLinkList = DoubleLinkList()
doubleLinkList.weiChaFa()
print(doubleLinkList.search(3))
print(doubleLinkList.remove(3))
print(doubleLinkList.remove(3))

