# 基数排序
def radixSort(l):
    # 创建桶，0~9 共10个桶,分别记录0，1,2,3,4,5,6,7,8,9
    bucket =[[],[],[],[],[],[],[],[],[],[]]
    dev = 1
    maxNumberLen = 1 # 代表要比较的多少位数，1:代表只比较个位，2:代表十位 ...
    currentNumberLen  = 1
    while currentNumberLen <=maxNumberLen:
        # 比较列表中数字的所有个,十位...数，然后放入桶中
        for number  in l:
            bucket[(number//dev)%10].append(number)
            if len(str(number)) > maxNumberLen:
                maxNumberLen = len(str(number))
        index = 0
        # 从桶中取出来，排列成一个新的序列
        for k,alist in enumerate(bucket):
            for n in alist:
                l[index] = n
                index +=1
            bucket[k] = [] # 清空桶里的元素
        dev *=10
        currentNumberLen +=1
    return l

print(radixSort([123, 91, 1, 97, 17, 23, 84, 28, 72, 5, 67, 25]))




