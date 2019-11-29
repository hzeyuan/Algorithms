"""
给定一个头结点为 root 的链表, 编写一个函数以将链表分隔为 k 个连续的部分。

每部分的长度应该尽可能的相等: 任意两部分的长度差距不能超过 1，也就是说可能有些部分为 null。

这k个部分应该按照在链表中出现的顺序进行输出，并且排在前面的部分的长度应该大于或等于后面的长度。

返回一个符合上述规则的链表的列表。

举例： 1->2->3->4, k = 5 // 5 结果 [ [1], [2], [3], [4], null ]
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def splitListToParts(root, k):
    # 一开始能想到的方法
    # 先找到长度
    if root:
        head = root
        length = 1
        while head.next:
            length  +=1
            head = head.next
        # length//k 为平均的部分的长度，length%k为多出来的部分长度
        averageLength = length//k
        moreLength = length%k
        resultList =[]
    # 长度不为0时，循环
    for i in range(k):
        if root:
            resultList.append(root)
            if length >k:
                if moreLength >0:
                    partLength = averageLength
                else:
                    partLength = averageLength-1
            else:
                partLength =0
            while partLength:
                root = root.next
                partLength -=1
            newRoot = root.next
            root.next = None
            root =newRoot
            moreLength -=1
        else:
            resultList.append(None)
    return  resultList


A = ListNode(1)
B = ListNode(2)
C = ListNode(3)
D = ListNode(4)
A.next = B
B.next = C
C.next = D

splitListToParts(A,5)
print(A)
