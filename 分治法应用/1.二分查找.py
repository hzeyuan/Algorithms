# 二分查找
def binarySearch(l,data):
    start =0
    index = len(l)//2
    end  = len(l)
    while start<=index<end:
        if data <l[index]:
            index  = (index+start)//2
        elif data >l[index]:
            index = (index+end)//2
        else:
            return index

print(binarySearch([1,2,3,4,5,6],6))