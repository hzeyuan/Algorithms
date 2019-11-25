# 定义一个节点
class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None
    def setLeft(self,left):
        self.left = left
        return self
    def setRight(self,right):
        self.right = right
        return self
'''
来模拟这棵树的存储
     1
    / \
   2   3
  /
  4
'''

def createTree():
    n4 = Node(4)
    n2 = Node(2).setLeft(n4)
    n3 =Node(3)
    n1 = Node(1).setLeft(n2).setRight(n3)
    return n1


t = createTree()
print(t.data)