# 插入排序,
def insertionSort(alist):
    for k , v in enumerate(alist): # v 是要插入的值
        index = k # 记录当前的下标
        while index >0  and alist[index-1] >v: ##从下标1开始插入，也就是第二个
            alist[index] = alist[index-1]
            index -=1 # 从后往前插入比较,看是否更合适的插入点
        alist[index] = v # 插入


# 插入2的时候的比较
# 34521
# 34551
# 34451
# 33451
# 23451 alist[0] = 2

# 插入1 的时候的比较
# 23451
# 23455
# 23445
# 23345
# 22345
# 12345


print(insertionSort([3,4,5,2,1]))
