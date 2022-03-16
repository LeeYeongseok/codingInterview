import sys

class stack:
    def __init__(self):
        self.stack = []
    
    def push(self, n):
        self.stack.append(n)
        
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return "비어있음"
        
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return "비어있음"
        
    def isEmpty(self):
        if len(self.stack) > 0:
            return False
        else:
            return True

def sort(left : stack):
    right = stack()
    while not left.isEmpty():
        temp = left.pop()    
        while not right.isEmpty() and right.peek() < temp:
            left.push(right.pop())
        right.push(temp)
    return right

newStack = stack()
count = int(input())
    
for i in range(count):
    newStack.push(int(input()))

newStack = sort(newStack)
print(newStack.stack)