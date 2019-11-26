# 快速排序
# 按照基准值划分
def pivotPartition(l,left,right):
    index = left
    pivot = l[left] # 第一个元素为基准值
    # 右指针中找到比基准值小的数
    while left <right:
        while l[right] > pivot and left <right:  # 当右指针的元素 > 基准值,指针数减少1
            right -=1
        # 左指针中找到比基准值大的数字
        while l[left] <= pivot and left < right: # 当左指针的元素 > 基准值,指针数增加1
            left +=1
        # 交换这两个数字
        l[left],l[right] = l[right],l[left]
    # 当left == right时，交换基准值和left上的值
    l[left],l[index] = pivot,l[left]
    return left

def quickSort(l,left,right):
    if left >= right:
        return
    else:
        pivot = pivotPartition(l,left,right)
        quickSort(l,left,pivot-1)
        quickSort(l,pivot+1,right) # 这里指针指向 增量的后一位，要不然会报错栈溢出
    return l

print(quickSort([3,1,2,5,4],0,4))

# 非递归版本
def quickSort2(l,left,right):
    pivot = pivotPartition(l,left,right)
    while pivot>left:
        pivot =  pivotPartition(l,left,pivot-1)
    while pivot<right:
        pivot = pivotPartition(l,pivot+1,right)
    return l
l = [3,1,2,5,4,7,4,-1]
print(quickSort2(l,0,len(l)-1))