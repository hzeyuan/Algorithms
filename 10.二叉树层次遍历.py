from collections import deque

# 定义一个节点
class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

    def setLeft(self, left):
        self.left = left
        return self

    def setRight(self, right):
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
    n3 = Node(3)
    n1 = Node(1).setLeft(n2).setRight(n3)
    return n1


t = createTree()


# 层序遍历,利用队列的特性
def printBinarySearchTree(tree):
    t = tree
    l = []
    queue = []
    queue.append(t) # 先将跟节点入队
    while queue: # 队列不为空
        node = queue.pop(0)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

        l.append(node.data)

    return l
print(printBinarySearchTree(t))
