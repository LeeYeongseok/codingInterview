import sys

def nextNode(tree, index):
    # 오른쪽 자식노드가 존재한다면 오른쪽 자식노드의 가장 왼쪽 노드
    if index*2+1 < len(tree) and tree[index*2+1] != None:
        index = index * 2 + 1
        while index*2 < len(tree) and tree[index*2] != None:
            index = index*2
        return tree[index]
    # 오른쪽 자식 노드가 없으면 더이상 해당 노드가 오른쪽 노드가 아닐때 까지 올라간다
    else:
        while index%2 == 1:
            index = index // 2
        index = index // 2
        return tree[index]

tree = [None, 7, 4, 9, 2, 6, 8, 10, 1, 3, 5, None, None]

print(nextNode(tree, 4))
print(nextNode(tree, 5))