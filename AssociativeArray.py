'''Simple Associative Array class'''
''' This is a basic data structure allowing for constant time access
(of course, python has a built in dictionary type that is far more versatile
so you wouldn't actually need to use something like this.)'''

class Node:
    def __init__(self,k,v):
        self.key = k
        self.value = v

class AsscArrayType:
    def __init__(self,ArrayOfNodes):
        self.ArrayOfNodes=ArrayOfNodes
    def GetValue(self,key):
        for AsscPair in AsscArray :
            if AsscPair.key== key: return AsscPair.value

AsscArray = []
for x in range(10):
    AsscArray.append(Node(x,"Hello"+str(x)))

HelloAsscArray = AsscArrayType(AsscArray)
print (HelloAsscArray.GetValue(2))
