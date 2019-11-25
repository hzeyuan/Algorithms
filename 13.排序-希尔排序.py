# 希尔排序
def shellSort(l):
    subListCount  = len(l)//2 # 设定的增量
    while subListCount >0:
        # 分组
        for i in range(subListCount):
            # 组内部进行插入排序
            gapInsertionSort(l,i,subListCount)
        subListCount //=2
    return l
# 这就是一个插入排序,只是列表不在是连续的了，而是有了间隔
def gapInsertionSort(l,start,gap):
    # 循环组,这里间隔gap得到一个组
    for i in range(start,len(l),gap):
        index = i
        value = l[i]

        while  index+1 >gap and l[index-gap] >value:
            l[index] = l[index - gap]
            index -=gap
        l[index] = value


print(shellSort([5,3,2,1,4]))