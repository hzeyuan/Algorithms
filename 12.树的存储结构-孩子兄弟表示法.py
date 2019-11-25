class Node:
    def __init__(self,data,child):
        self.data = data
        self.child = child
        self.sibling = None

L = Node('L',None)
K = Node('K',None)
F = Node('F',None)
E = Node('E',[K,L])
B = Node('B',[E,F])
G = Node('G',None)
C = Node('C',[G])
M = Node('M',None)
H = Node('H',[M])
I = Node('I',None)
J = Node('J',None)
D = Node('D',[H,I,J])
A = Node('A',[B,C,D])

print(A)

def forestConvertBinaryTree(tree):


    stack = [tree]
    # 加线 就是记录节点的兄弟节点
    while stack: # 栈不为空
        tree =  stack.pop(0)
        if  tree.child:
            index = 0
            for node in tree.child:
                if index<len(tree.child)-1:
                    node.sibling = tree.child[index+1]
                print(node.data)
                # 兄弟节点之间加线
                index +=1
                stack.append(node)
            # 去线：对树中每个结点，只保留它与第一个孩子结点的连线，删除它与其他孩子结点之间的连线。
            tree.child = [tree.child[0]]

forestConvertBinaryTree(A)
print(A)


