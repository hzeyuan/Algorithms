class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next

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
