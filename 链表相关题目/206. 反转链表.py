"""
反转一个单链表。
"""

"""
这道题的思路是,遍历链表，让链表中的指针都指向前一个节点
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def reverseList(head: ListNode) -> ListNode:
    if not head:
        return None
    preNode =None
    while head.next:
        currentNode =head
        tmp = head.next
        currentNode.next = preNode
        preNode = head  # 上一个节点
        head = tmp
    head.next = preNode # 最后一个节点指向前面的节点，因为前面的节点的指针都已经修改成了指向上一个节点,所以整个链表完成了反转
    return head

A = ListNode(1)
B = ListNode(2)
C = ListNode(3)
D = ListNode(4)
#E = ListNode(5)
A.next = B
B.next = C
C.next = D
#D.next = E

print(reverseList(A))