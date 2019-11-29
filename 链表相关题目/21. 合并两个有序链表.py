"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
"""

"""
思路，用一个指针，指向两条链表，同时比较大小结果后，指针指向数字较小的节点，同时该节点位置+1，直到链表结束，在把剩余的的链表添加到新的链表中。
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if not l1:
        return l2
    elif not l2:
        return l1
    elif not l1 and not l2:
        return None
    head = ListNode(-1)
    tail = head
    # 两条链表的都不为空
    while l1 and l2:
        if l1.val <=l2.val:
            tail.next = l1
            l1 =l1.next
        elif l1.val >l2.val:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    if  l1 != None:
       tail.next = l1
    else:
       tail.next =l2
    return head.next

A = ListNode(-9)
B = ListNode(3)

A.next = B



A1 = ListNode(5)
B1 = ListNode(7)

A1.next = B1



print(mergeTwoLists(A,A1))
