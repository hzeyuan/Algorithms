# 这道题的关键是，发现旋转数组中的首元素肯定不小于元旋转数组的尾元素
def minNumberInRotateArray(l,start,end):
    if not l:
        return None
    if l[start] < l[end]:
        return l[start]
    mid =(start+end)//2
    if start ==mid:
        return l[start]
    if l[mid] < l[start]: #中间数 小于首元素，最小数在前半部分
        return minNumberInRotateArray(l,start,mid)
    elif l[mid] >=l[start]: #中间数 大于首元素，最小数在后半部分
        return minNumberInRotateArray(l,mid+1,end)


print(minNumberInRotateArray([3, 4, 5, 1, 2],0,4))
print(minNumberInRotateArray([1, 2, 3, 4, 5],0,4))
print(minNumberInRotateArray([1, 1, 1, 0, 1],0,4))
print(minNumberInRotateArray([1, 0, 1, 1, 1],0,4))
