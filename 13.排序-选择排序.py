# 选择排序，每次从准备排序的列表中，挑一个最小或(最大)的出来，慢慢的列表就空了。
def selectSort(l):
    for k ,v in enumerate(l):
        index= 0 # index用来记录 最小的数的下标
        smallNumber = float('inf')
        for i in range(k,len(l)):# 挑一个最小的数出来
            if l[i] < smallNumber:
                smallNumber = l[i]
                index= i
        # 更换，index和k下标上两者的值
        l[k],l[index] = smallNumber,l[k]
    return l

print(selectSort([54,26,93,17,77,31,44,55,20]))