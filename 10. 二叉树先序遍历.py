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


# 先序遍历 递归版本

def printTree(tree, l):
    if tree:
        l.append(tree.data)
        printTree(tree.left, l)
        printTree(tree.right, l)
    return l


l = printTree(t, [])
print(l)


# 先序遍历，非递归版本，依靠栈来实现
def printTree1(tree):
    l = []
    stack = [tree]  # 根节点
    while stack:  # 当栈为空时，退出循环
        p = stack.pop()  # 弹出节点
        while p:
            l.append(p.data)  # 把节点中的值添加到列表中，打印
            if p.right:  # 如果节点有右子树，压入栈
                stack.append(p.right)
            p = p.left  # 节点一直指向左子树
    return l


print(printTree1(t))
