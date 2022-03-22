import sys
import math

class linkedTree:
    def __init__(self, sortedList):
        self.sortedList = sortedList
        self.treeList = [None for _ in range(2 * len(sortedList))]
        self.BST(sortedList, 1)
        
    def BST(self, sortedList, index):
        if len(sortedList) == 1:
            self.treeList[index] = sortedList[0]
            return
        if not sortedList:
            return
        self.treeList[index] = sortedList[len(sortedList)//2]
        self.BST(sortedList[:len(sortedList)//2], index*2)
        self.BST(sortedList[len(sortedList)//2+1:], index*2+1)

def checkHeight(tree, index):
    # 더 하위 노드가 없으면 -1 리턴 
    if index >= len(tree):
        return -1
    
    # 해당 노드가 NULL이면 -1 리턴
    if tree[index] == None:
        return -1
 
    # 왼쪽 오른쪽 둘중 한곳이라도 다른 높이를 가지고 있다면 음의 무한대 값을 리턴
    leftHeight = checkHeight(tree, index*2)
    if leftHeight == -math.inf:
        return -math.inf
    
    rightHeight = checkHeight(tree, index*2+1)
    if rightHeight == -math.inf:
        return -math.inf
    
    #왼쪽 오른쪽 높이를 비교해서 1을 초과하는 차이가 있으면 음의 무한대 값을 리턴
    heightDiff = leftHeight - rightHeight
    if abs(heightDiff)>1:
        return -math.inf
    #그렇지 않으면 더 큰 높이에 1을 더한값을 현재 노드의 높이로  리턴
    else:
        return max(leftHeight, rightHeight) + 1
    
sortedList = list(map(int, sys.stdin.readline().split()))
treeA = linkedTree(sortedList)
print(treeA.treeList)

notValancedList = [None, 1, 1, None, 3, 4]

if checkHeight(treeA.treeList, 1) != -math.inf:
    print("valanced")
else:
    print("not valanced")
    
if checkHeight(notValancedList, 1) != -math.inf:
    print("valanced")
else:
    print("not valanced")