# 归并排序

# 排序且合并
def megre(l,start,end,index):
    newL= []
    leftList = l[start:index]
    rightList = l[index:end]
    for v1, v2 in zip(leftList, rightList):
        if v1 < v2:
            newL.append(v1)
            newL.append(v2)
        else:
            newL.append(v2)
            newL.append(v1)
    if len(leftList) < len(rightList):
        newL.append(*rightList[len(leftList):])
    elif len(leftList) > len(rightList):
        newL.append(*leftList[len(rightList):])

    l[start:end] = newL

def megreSort(l,start,end):

    if start == end:
        return
    else:
        index =(start+end)//2
        # 将数组切割，直到数组的长度为1
        megreSort(l,start,index)
        megreSort(l,index+1,end)
        # 将 分割的数组进行排序
        megre(l,start,end,index)

    return l

# 模拟一下 函数执行的过程
# 首先 [3,1],[2,4,5]
# [3],[1] ,[2,4,5]
# [3],[1], [2],[4,5]
# [3],[1],[2],[4],[5]
# 两两排序合并
# [1,3] [2],[4,5]
# [1,3] [2,4,5]
# [1,2,3,4,5]

print(megreSort([3,1,2,4,5],0,5))




