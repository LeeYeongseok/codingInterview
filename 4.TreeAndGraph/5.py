import sys
import math

def checkBST(tree, index, max = None, min = None):
    #해당 노드가 NULL이라면 true 리턴
    if index >= len(tree):
        return True
    if tree[index] == None:
        return True
    
    #해당 노드가 존재
    
    #해당 노드가 범위 내에 속하지 않으면 False
    if (min != None and tree[index] <= min) or (max != None and tree[index] >= max):
        return False
    
    #둘중 하나라도 이진트리를 만족하지 않으면 False
    if (index*2 < len(tree) and not checkBST(tree, index*2, max=tree[index])) or (index*2+1 < len(tree) and not checkBST(tree, index*2+1, min=tree[index])):
        return False
    #해당 노드의 좌우에 대해서 양쪽 다 이진탐색트리를 만족하면 True
    else:
        return True
    
def ifBST(tree):
    return checkBST(tree, 1)
    
A = [None, 7, 4, 9, 2, 6, 8, 10, 1, 3, 5]

B = [None, 7, 4, 9, 2, 6, 8, 10, 1, 3, 5, None, None, None]

C = [None, 7, 4, 9, 1, 6, 8, 10, 2, 3, 5, None, None, None]

print(ifBST(A))
print(ifBST(B))
print(ifBST(C))