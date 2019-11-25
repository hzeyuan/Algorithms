## 先定义节点
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

class Stack:
    def __init__(self):
        self.head = None

    # 入栈
    def push(self,data):
        temp = Node(data)  # 建造一个节点，并初始值为data
        temp.setNext(self.head)  # 节点指针指向头指针
        self.head = temp
    # 出栈
    def pop(self):
        if self.head == None:
            return -1
        else:
            data = self.head.getData()
            self.head = self.head.getNext()
        return data
    # 判断是否为空
    def isEmpty(self):
        return True if self.head == None else False
    # 遍历
    def print(self):
        l = []
        current = self.head
        while current!=None:
            l.append(current.getData())
            current = current.getNext()
        return l
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.print())
print(s.pop())
print(s.print())
print(s.isEmpty())