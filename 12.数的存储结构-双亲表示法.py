# 双亲表示法
class PTNode:
    def __init__(self,data,parent):
        self.data = data
        self.parent = parent
    # 当属性相同时，就判断别为相同
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

class tree:
    def  __init__(self,data):
        self.root = PTNode(data,-1)
        self.list = [self.root]
    def addNode(self,data,parent):
        index = 0
        for item in self.list:
            if item.data ==parent:
                break
            index +=1
        self.list.append(PTNode(data,index))
        return self
    def getNodeIdx(self,Node):
        index = 0
        for item in  self.list:
            if item == Node:
                return  index
            index += 1

t = tree('R') #根节点
nodeAIdx = t.getNodeIdx(PTNode('A',-1))
t.addNode('A','R').addNode('B','R').addNode('C','R')
t.addNode('D','A').addNode('E','A')
t.addNode('F','C')
t.addNode('G','F').addNode('H','F').addNode('K','F')

# 孩子表示法


