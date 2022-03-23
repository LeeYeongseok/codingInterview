

class Node:
    
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        
    def addNode(self, data):
        nowNode = self
        while True:
            if nowNode.data >= data:
                if nowNode.left == None:
                    nowNode.left = Node(data)
                    break
                nowNode = nowNode.left
                
            else:
                if nowNode.right == None:
                    nowNode.right = Node(data)
                    break
                nowNode = nowNode.right
    
    def inorder(self, node=None, level=1):
        if not node and level == 1:
            node = self
        if node:
            ansList = self.inorder(node.left, level+1) + [node.data] + self.inorder(node.right, level+1)
            return ansList
        return [None]
    
    def preorder(self, node=None, level=1):
        if not node and level == 1:
            node = self
        if node:
            ansList =  [node.data]+  self.preorder(node.left, level+1) + self.preorder(node.right, level+1)
            return ansList
        return [None]
    
treeA = Node(5)
treeA.addNode(3)
treeA.addNode(2)
treeA.addNode(4)
treeA.addNode(7)
treeA.addNode(6)
treeA.addNode(8)

treeB = Node(3)
treeB.addNode(2)
treeB.addNode(4)

print(treeA.inorder())
print(treeA.preorder())
print(treeB.preorder())
if treeB.preorder() in treeA.preorder():
    print(True)
else:
    print(False)