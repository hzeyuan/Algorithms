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

class queue:
    def __init__(self,QueueSize):
        self.arr = [None]*(QueueSize+1)#牺牲一个储存单元来，辨别空还是满
        self.front = 0 # 队头指针
        self.rear = 0 # 队尾指针
    # 入队
    def enqueue(self,data):
        QueueSize = len(self.arr)
        self.arr[self.rear] = data
        self.rear  = (self.rear+1)%QueueSize
    # 出队
    def dequeue(self):
        QueueSize = len(self.arr)
        self.arr[self.front] = None
        self.front = (self.front+1)%QueueSize
    # 判断是否空队列
    def isEmpty(self):
        return  True if self.rear == self.front else False
    # 判断是否满度列
    def isFull(self):
        QueueSize = len(self.arr)
        return True if  self.front == (self.rear+1)%QueueSize else False
    # 判断已经存储的长度
    def size(self):
        return (self.rear - self.front+len(self.arr))% len(self.arr)

q = queue(3)
q.enqueue(1)
q.enqueue(2)
print(q.size())
q.enqueue(3)
print(q.arr)
print("队满",q.isFull())
q.dequeue()
print(q.arr)
q.dequeue()
print(q.arr)
q.dequeue()
print(q.arr)
print("队空",q.isEmpty())
