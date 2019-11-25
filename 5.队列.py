class Queue:
    def __init__(self):
        self.items = []
    # 判空
    def isEmpty(self):
        return self.items == []
    # 入队
    def enqueue(self,item):
        self.items.insert(0,item)
    # 出队
    def dequeue(self):
        return self.items.pop()
    # 判断队列长度
    def size(self):
        return len(self.items)
    def print(self):
        print(self.items)
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.print()
print(q.dequeue())
q.print()
q.enqueue(4)
q.print()
print(q.isEmpty())