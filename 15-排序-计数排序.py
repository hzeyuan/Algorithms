# 计数排序
# 计数排序速度快于 比较排序算法,但需要大量的内存，当数字很大的时候
def countSort(l):
    # 找到最大值
    maxValue= max(l)
    bucket = [0]*(maxValue+1) #创建桶的数量，我们用下标来判断数字
    for n in l:
        bucket[n] +=1 # 下标为n的桶，计数加1
    # 计数完成后，我们在遍历出来
    index= 0
    for i,n in enumerate(bucket):
        while n >0:
            l[index] = i # 桶的下标就是元素的值，进行赋值操作
            index +=1 # 数组索引+1
            n-=1 #桶中的元素数量减1
    return l

print(countSort([123, 91, 1, 97, 17, 23, 84, 28, 72, 5, 67, 25]))
