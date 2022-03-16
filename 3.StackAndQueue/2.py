import sys

class stack:
    
    def __init__(self):
        self.stackList = []
        self.minstackList = []
    
    def push(self, n):
        if self.minNumber() >= n:
            self.minstackList.append(n)
        self.stackList.append(n)
        
    def pop(self):
        if len(self.stackList) == 0:
            return "빈 스택"
        popNum = self.stackList.pop()
        if self.minstackList[-1] == popNum:
            self.minstackList.pop()
        return popNum
    
    def minNumber(self):
        if len(self.stackList) == 0:
            return sys.maxsize
        return self.minstackList[-1]
    
newStack = stack()

while True:
    print("1. 푸시, 2. 팝, 3. 최소값")
    index = int(input())
    if index == 1:
        newStack.push(int(input())) 
    elif index == 2:
        print(newStack.pop())
    elif index == 3:
        print(newStack.minNumber())
    else:
        break
    print(newStack.stackList)
    print(newStack.minstackList)