#  当知道要删除的节点，可以快速删除节点
class ListNode():
    def __init__(self,data):
        self.data =data
        self.next =None
    def __del__(self):
        self.data =None
        self.next = None

def DeleteNode(head,toDeteleNode):
    if not head  or not toDeteleNode: # 如果没有根节点后者待删除的节点，返回None
        return None
    if head == toDeteleNode: # 带删除的节点为头结点
        head.__del__()
        toDeteleNode.__del__()
    elif  toDeteleNode.next !=None: # 待删除的节点既不是根节点，也不是最后一个节点
        nextNode = toDeteleNode.next
        toDeteleNode.data = nextNode.data
        toDeteleNode.next = nextNode.next
        nextNode.__del__()
    else: # 待删除的节点是最后一个节点
        nextNode = head
        while nextNode.next !=toDeteleNode:
            nextNode = nextNode.next
        nextNode.next =None
        toDeteleNode.__del__()

node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node4 = ListNode(15)
node1.next = node2
node2.next = node3
node3.next = node4

DeleteNode(node1,node2)