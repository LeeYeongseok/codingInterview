import sys
import math
   
   
#링크드리스트를 만들 노드
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        
    def add(self, data):
        node = self
        while node.next:
            node = node.next
        node.next = Node(data)

    def printList(self):
        node = self
        while node.next:
            node = node.next
            print(node.data, end=' ')
        print('')
    
class linkedTree:
    def __init__(self, sortedList):
        self.sortedList = sortedList
        self.treeList = [None for _ in range(2 * len(sortedList))]
        self.BST(sortedList, 1)
        self.levelList = [Node() for _ in range(int(2+math.log2(len(self.treeList))))]
        self.link(1, 1)
        
    def BST(self, sortedList, index):
        if len(sortedList) == 1:
            self.treeList[index] = sortedList[0]
            return
        if not sortedList:
            return
        self.treeList[index] = sortedList[len(sortedList)//2]
        self.BST(sortedList[:len(sortedList)//2], index*2)
        self.BST(sortedList[len(sortedList)//2+1:], index*2+1)
        
    def link(self, index, level):
        if index >= len(self.treeList):
            return
        if self.treeList[index] == None:
            return
        self.levelList[level].add(self.treeList[index])
        self.link(index*2, level+1)
        self.link(index*2+1, level+1)
        
    
sortedList = list(map(int, sys.stdin.readline().split()))
treeA = linkedTree(sortedList)
print(treeA.treeList)
for i in treeA.levelList:
    i.printList()
