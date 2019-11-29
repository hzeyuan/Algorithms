'''
给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。

请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。
'''

"""
这道题的思路就是，每一个节点都指向他的下下个节点，保留最后一个节点和倒数第二个节点，
当链表为奇数时，最后一个节点连接第二个节点
当链表为偶数时，倒数第二个节点连接第二个节点
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def oddEvenList(head: ListNode) -> ListNode:
    if not head:
        return None
    oddRoot= head # 奇数链表
    evenRoot = head.next # 偶数链表
    preNode =None# 尾巴节点的前一个节点
    length =1
    # 遍历节点
    while oddRoot.next:
        # 我们让每个节点的指针都指向他的下下个节点
        currentNode = oddRoot
        # 获得倒数第二个节点
        if oddRoot.next.next == None:
            preNode = oddRoot
        newRoot = oddRoot.next
        if  oddRoot.next.next:
            currentNode.next = oddRoot.next.next
        else:
            currentNode.next = None

        oddRoot = newRoot

        length +=1
    if length %2==0:
        preNode.next = evenRoot
    else:
        oddRoot.next = evenRoot
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

print(oddEvenList(A))