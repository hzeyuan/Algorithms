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


# 后序序遍历 递归版本

def printTree(tree, l):
    if tree:
        printTree(tree.right, l)
        l.append(tree.data)
        printTree(tree.left, l)
    return l


l = printTree(t, [])
print(l)


# 后序遍历，非递归版本，依靠栈来实现
def printTree1(tree):
    l = []
    p = tree
    stack = []  # 栈
    while stack or p:  # 当栈为空时，退出循环
        if p:  # 入栈，同时继续指向右子树
            stack.append(p)
            p = p.right
        else:  # 出栈，打印，节点指向左子树
            p = stack.pop()
            l.append(p.data)
            p = p.left

    return l


print(printTree1(t))
