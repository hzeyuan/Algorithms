# 如果一棵完全二叉树的任意一个非终结点的元素都不小于其子结点，则此二叉树称为最大堆。

class maxHeap:
    def  __init__(self,l):
        self.heapList = l
        self.currentSize = 0

    # 构建堆
    def buildHeap(self):
        for i in range(len(self.heapList)//2,-1,-1):
            self.heapify(i)
        return self.heapList
    # 查找堆中的元素,利用栈来实现
    def find(self,data):
        stack = [0]
        while stack: # 栈不为空
            start =stack.pop(0) # 出栈
            if self.heapList[start] >data: #节点大于要查找的数字
                if start*2+1<len(self.heapList) and self.heapList[start*2+1] >=data: #判断其左孩子是否需要入栈
                    stack.append(start*2+1)
                if start*2+2<len(self.heapList) and  self.heapList[start*2+2] >=data:#判断其右孩子是否需要入栈
                    stack.append(start*2+2)
            elif self.heapList[start] == data:
                return start
        return -1

    # 插入元素
    def insert(self,data):
        self.heapList.append(data)
        index = len((self.heapList))-1
        while  index!=0  and  data > self.heapList[index//2]:
            self.heapList[index] = self.heapList[index//2]
            index //=2
        self.heapList[index] = data
        return self.heapList
    # 删除元素
    def remove(self,data):
        index = self.find(data)
        if index == -1:
            return index
        else:
            self.heapList[index],self.heapList[-1] = self.heapList[-1],self.heapList[index]# 交换要删除的元素，和最后一个元素
            self.heapList.pop()# 弹出最后一个元素
            self.heapify(index)# 重新排列最后index后面的树，使其满足堆的特性

        return self.heapList
    # 递归
    def heapify(self, i):
        l = self.heapList
        left = 2 * i + 1  # 左孩子
        right = 2 * i + 2  # 右孩子
        lastgest = i  # 最大的数字
        if left < len(l) and l[left] > l[lastgest]:
            lastgest = left
        if right < len(l) and l[right] > l[lastgest]:
            lastgest = right
        if lastgest != i:
            l[i], l[lastgest] = l[lastgest], l[i]
            self.heapify(lastgest)

    # 非递归
    def heapify1(self, i):
        l = self.heapList
        lastgest = None
        while lastgest !=i:
            left = 2 * i + 1  # 左孩子
            right = 2 * i + 2  # 右孩子
            lastgest = i  # 最大的数字
            if left < len(l) and l[left] > l[lastgest]:
                lastgest = left
            if right < len(l) and l[right] > l[lastgest]:
                lastgest = right
            if lastgest != i:
                l[i], l[lastgest] = l[lastgest], l[i]
                i = lastgest
                lastgest = -1


m =maxHeap([12, 91, 1, 97, 17, 23, 84, 28, 72, 5, 67, 25])
print(m.buildHeap())
print(m.find(12))
print(m.insert(27))
print(m.remove(12))