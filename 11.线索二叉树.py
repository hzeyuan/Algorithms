# 定义一个节点
class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None
        self.ltag = 0
        self.rtag = 0

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
  / \
  4  5
'''




class BinaryTree:
    def __init__(self,array):
        self.root = Node(array[0])
        self.preNode =None
        deque = [self.root]
        for  i in range(1,len(array),2):
            node = deque.pop(0)
            if node:
                if not node.left and i <len(array):
                    node.setLeft(Node(array[i]))
                    deque.append(node.left)
                if not node.right and i+1 <len(array):
                    node.setRight(Node(array[i+1]))
                    deque.append(node.right)

    # 先序遍历 二叉树线索化
    def PreBinarySearchTree(self,tree=None):
        if tree:
            if not tree.left:
                tree.left  = self.preNode
                tree.ltag = 1
            if self.preNode!=None and not  self.preNode.right:
                self.preNode.right = tree
                self.preNode.rtag = 1
            print("上一个节点:", self.preNode.data if self.preNode else 'none', "当前节点:", tree.data)
            self.preNode = tree
            if tree.ltag ==0:
                self.PreBinarySearchTree(tree.left)
            if tree.rtag==0:
                self.PreBinarySearchTree(tree.right)
    # 中序遍历 二叉树线索化
    def MiddleBinarySearchTree(self,tree=None):
        if tree:
            self.MiddleBinarySearchTree(tree.left)
            if not tree.left:
                tree.ltag = 1  # 标记
                tree.left = self.preNode  # 当前节点的左孩子为上一个节点
            if self.preNode != None and not self.preNode.right:
                self.preNode.rtag = 1  # 标记
                self.preNode.right = tree  # 上一个节点的右孩子为当前节点
            print("上一个节点:", self.preNode.data if self.preNode else 'none', "当前节点:", tree.data)
            self.preNode = tree  # 定义当前节点 为 下一次循环中的上一个节点
            self.MiddleBinarySearchTree(tree.right)
        return

    # 后序遍历，二叉树线索化
    def LastBinarySearchTree(self,tree=None):
        if tree:
            if tree.ltag==0:
                self.LastBinarySearchTree(tree.left)
            if tree.rtag==0:
                self.LastBinarySearchTree(tree.right)
            if not tree.left:
                tree.left = self.preNode
                tree.ltag =1
            if self.preNode!=None and  not self.preNode.right:
                self.preNode.right=tree
                self.preNode.rtag = 1
            print("上一个节点:", self.preNode.data if self.preNode else 'none', "当前节点:", tree.data)
            self.preNode = tree
    # 先序线索二叉树，遍历
    def printPreBinarySearchTree(self):
        tree = self.root  # 树的根节点
        while tree:  # 从最左边的孩子开始 循环
            print(tree.data)
            if tree.rtag == 1:  # 找到其后继节点，然后指针指向后继节点
                tree = tree.right
            else:  # 如果不是后继节点，是其右孩子
                if tree.left and tree.ltag!=1:
                    tree = tree.left
                else:
                    tree = tree.right

    # 中序线索二叉树 遍历
    def printMiddleBinarySearchTree(self):
        tree = self.root # 树的根节点
        while tree.left: # 先找树的最左边的孩子
            tree = tree.left
        while tree: # 从最左边的孩子开始 循环
            print(tree.data)
            if tree.rtag ==1: #找到其后继节点，然后指针指向后继节点
                tree = tree.right
            else: # 如果不是后继节点，是其右孩子
                tree = tree.right # 则指针指向其右孩子
                if tree:
                    while tree.ltag == 0: # 循环当前右孩子树中的最左边的节点
                        tree = tree.left




t =BinaryTree([1,2,3,4,5,6,7])

#t.PreBinarySearchTree(t.root)
#t.printPreBinarySearchTree()
#t.MiddleBinarySearchTree(t.root)
#t.printMiddleBinarySearchTree()






