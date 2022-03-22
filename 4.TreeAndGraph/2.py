import sys


sortedList = list(map(int, sys.stdin.readline().split()))
treeList = [0 for _ in range(2 * len(sortedList))]

def BST(sortedList, index):
    global treeList
    if len(sortedList) == 1:
        treeList[index] = sortedList[0]
        return
    if not sortedList:
        return      
    
    treeList[index] = sortedList[len(sortedList)//2]
    BST(sortedList[:len(sortedList)//2], index*2)
    BST(sortedList[len(sortedList)//2+1:], index*2+1)
    
    
BST(sortedList,1)
print(treeList)