class CTNode:
    def __init__(self,data,index):
        self.data =data
        self.index = index
        self.next = None

class tree:
    def __init__(self,l):
        index = 0
        self.list = []
        for item in l:
            self.list.append(CTNode(item,index))
            index += 1
    def getNode(self,data):
        for item in self.list:
            if item.data == data:
                return item
    def addChild(self,node,child):
        while node.next:
            node = node.next
        node.next = child



t = tree(['R','A','B','C','D','E','F','G','H','K'])
# R -> A -> B -> C
t.addChild(t.getNode('R'),t.getNode('A'))
t.addChild(t.getNode('R'),t.getNode('B'))
t.addChild(t.getNode('R'),t.getNode('C'))

# A -> D -> E
t.addChild(t.getNode('A'),t.getNode('D'))
t.addChild(t.getNode('A'),t.getNode('E'))

# C -> F
t.addChild(t.getNode('C'),t.getNode('F'))

# F -> G -> H -> K
t.addChild(t.getNode('F'),t.getNode('G'))
t.addChild(t.getNode('F'),t.getNode('H'))
t.addChild(t.getNode('F'),t.getNode('K'))