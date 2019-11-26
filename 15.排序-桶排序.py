# 桶排序
def bucketSort(l):
    # 首先将数组中的元素映射到桶中去
    # 桶的数量为(最大值-最小值)+1
    # 映射函数，通过((元素值)-数组最小值)//桶数的映射关系来映射,映射关系可以换成其他的，这里只是示范
    maxN = max(l)
    minN = min(l)
    bucket = [[] for i in range((maxN-minN)+1)]
    # 映射到桶中
    for n in l:
        bucket[(n-minN)//5].append(n)
    index= 0
    # 对每个桶中的元素进行排序,这里我们使用冒泡排序
    for alist in bucket:
        # 冒泡排序
        for i in range(len(alist)):
            for j in range(i+1,len(alist)):
                if alist[i] > alist[j]:
                    alist[i], alist[j] = alist[j], alist[i]
        # 排序完以后，在添加回l中
        for n in alist:
            l[index] = n
            index +=1
    return l

print(bucketSort([12, 91, 1, 97, 17, 23, 84, 28, 72, 5, 67, 25]))