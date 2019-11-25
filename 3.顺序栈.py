#模拟顺序栈的基本操作
class stack:
    def __init__(self):
        self.stack = [] #用列表来表示
    # 入栈
    def push(self,data):
        self.stack.append(data)
    # 出栈
    def pop(self):
        return self.stack.pop(0)
    # 清空栈
    def clear(self):
        return self.stack.clear()
    # 遍历栈
    def printStack(self):
        print(self.stack)
        return self.stack
    # 判断栈是否为空
    def isEmpty(self):
        return False  if self.stack else True
s = stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.printStack()
s.pop()
s.printStack()
s.pop()
s.printStack()
s.clear()
print(s.isEmpty())
s.printStack()

