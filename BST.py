# A simple Binary Search Tree implemented in python. Constituent nodes are associative, i.e., 
# they contain both a key and value pair, the former being usable to reference the latter.

#binary seach tree
class BST:
    class Node:
        def __init__(self,key,value,SubrootNodes):
            self.key = key
            self.value = value
            self.SubrootNodes = SubrootNodes
            self.left = None
            self.right = None

    def size(self, somenode):
        if (somenode == None):
            return 0
        else:
            return somenode.SubrootNodes
        
    def get(self,x,key):
        if (x == None): return None
        if (key<x.key): return self.get(x.left,key)
        elif (key>x.key): return self.get(x.right,key)
        else: return x.value;
        
    def put(self,x,key,value):
        if (x == None): return self.Node(key,value,1)
        if (key<x.key): x.left = self.put(x.left, key, value)
        elif (key>x.key): x.right = self.put(x.right, key, value)
        else: x.value = value
        x.SubrootNodes = self.size(x.left) + self.size(x.right) + 1
        return x
    
    def test(self):
        Root = self.Node(1,"Hello",1)
        print "Putting into parent: " + str(self.put(Root,10,"Hola").key)
        print self.get(Root,10)

myBST = BST()
myBST.test()



