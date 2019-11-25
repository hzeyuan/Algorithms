# 冒泡排序 时间复杂度为 O(n2)
def  bubbleSort(l):
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]>l[j]:
                l[i],l[j] = l[j],l[i]
    return l




print(bubbleSort([3,4,5,2,1]))