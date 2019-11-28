### 简单的哈希表

class  Node:
    def __init__(self,key):
        self.key = key
        self.data = None
        self.next = None
class HashTable:
    def __init__(self,size):
        self.size = size
        self.array = [None] * self.size

    # 哈希函数,根据ASCII表中的值相加，除以表长度
    def hash(self,aString):
        num = 0
        for s in aString:
            num += ord(s)
        return num % self.size
    def get(self,key):
        slots = self.hash(key)
        head = self.array[slots]
        while head:
            if head.key == key: #找到相同的键
                break
            head = head.next
        if head == None: # 整条链表中都不存在相同的键，返回None
            return None
        else:
            return head.data
    def __setitem__(self, key, value):
        slots = self.hash(key)
        head = self.array[slots]
        if head == None: # 存放的数据是第一个数据，存在头结点
            self.array[slots] =Node(key)
            self.array[slots].data =value
        else:
            while head: # 遍历链表
                if head.key == key: #发现相同的键，修改值，跳出循环
                    head.data = value
                    break
                if head.next==None: # 判断节点是否到达尾部
                    head.next = Node(key)
                    head.next.data =value
                head = head.next
    def __getitem__(self, key):
        return self.get(key)

h = HashTable(11)
print("创建键值对")
h['fruits'] = 'apple'#创建键值对
h['car'] = 'baoma'
h['student'] = 'xiaoming'
h['sports'] = 'run'
print("创建键值对",h['fruits'],h['car'],h['student'],h['sports'])


h['sports'] = 'walk' # 修改键值对
print("修改键(sports)中的值为:",h['sports'])



h['sport1'] = 'test'
print("冲突的键值对(sports1)",h['sport1'])

print("不存在的键值对",h['fdsfds'])# 不存在的键
