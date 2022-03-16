import sys

class SetOfStacks:
    def __init__(self, size):
        self.stacks = [[]]
        self.numOfStacks = 0
        self.size = size
        
    def push(self, n):
        if len(self.stacks[self.numOfStacks]) >= self.size:
            self.stacks.append([])
            self.numOfStacks += 1
        self.stacks[self.numOfStacks].append(n)
        
    def pop(self):
        numPop = self.stacks[self.numOfStacks].pop()
        if len(self.stacks[self.numOfStacks]) == 0 and self.numOfStacks >= 1:
            self.stacks.pop()
            self.numOfStacks -=1
        return numPop
    
print("스택의 사이즈")
size = int(input())
setStack = SetOfStacks(size)

while True:
    print("1. 푸시 2.팝")
    c = int(input())
    print(setStack.stacks)
    if c == 1:
        setStack.push(int(input()))
    elif c == 2:
        print(setStack.pop())
    else:
        break