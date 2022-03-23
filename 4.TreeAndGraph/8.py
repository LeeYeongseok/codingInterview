import sys
import math


#같은 부모를 찾는방법
def findParent(a, b):
    
    #같은 높이가 될때까지
    while math.log2(a) != math.log2(b):
        if a > b:
            a = a // 2
        else:
            b = b // 2
    
    #같은 부모가 될때까지
    while a != b:
        a = a // 2
        b = b // 2
    
    return a

print(findParent(8,9))