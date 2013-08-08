#SimpleStack

class Node:
    def __init__(self,k,v):
        self.key = k
        self.next = v

class NodeContainer:
    def __init__(self,Top):
        self.Top = Top
    def push(self,pushedNode):
        temp = self.Top
        self.Top = pushedNode
        self.Top.next= temp
    def pop(self):
        temp = self.Top
        self.Top = self.Top.next 
        return temp

myStack= NodeContainer(Node(0,None))

for i in [x for x in range(10) if x%3 != 0 and x%4 != 0]:
    myStack.push(Node(i,None))

print (myStack.pop().key," | ", myStack.pop().key)
        
