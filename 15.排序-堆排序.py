# 堆排序
def heapSort(l):
    buildMaxHeap(l)
    length = len(l)-1
    while length >0:
        l[length] ,l[0] = l[0],l[length] # 交换跟节点和，最后一个节点
        l[:length] = buildMaxHeap(l[:length])
        length -= 1
    return l

# 构建最大堆
def buildMaxHeap(l):
    for i in range(len(l)//2,-1,-1):
        heapify(l,i)
    return l
def heapify(l,i):
    left = 2 * i + 1  # 左孩子
    right = 2 * i + 2  # 右孩子
    lastgest = i  # 最大的数字

    if left<len(l) and  l[left] > l[lastgest]:
        lastgest = left
    if right<len(l) and l[right] >l[lastgest]:
        lastgest = right
    if lastgest !=i:
        l[i],l[lastgest] = l[lastgest],l[i]
        #heapify(l,lastgest)
    return l


t = heapSort([12, 91, 1, 97, 17, 23, 84, 28, 72, 5, 67, 25])
print(heapify([12, 91, 1, 97, 17, 23, 84, 28, 72, 5, 67, 25],0))
#print(heapify1([12, 91, 1, 97, 17, 23, 84, 28, 72, 5, 67, 25],0))
print(t)