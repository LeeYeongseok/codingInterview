import sys

class queueStack:
    def __init__(self):
        self.stack=[]
        self.reverseStack=[]
    
    def push(self, n):
        #리버스 스택이 없으면 바로 삽입
        if not self.reverseStack:
            self.stack.append(n)
        
        #리버스 스택이 있으면 리버스 스택을 뒤집어서 가져오고 삽입
        else:
            self.stack = list(reversed(self.reverseStack))
            self.reverseStack.clear()
            self.stack.append(n)
        
    def popStack(self):
        #스택에 데이터가 없으면
        if not self.stack and not self.reverseStack:
            return "비어있음"
        #리버스 스택만 비어있으면 스택을 뒤집어서 pop
        if not self.reverseStack:
            self.reverseStack = list(reversed(self.stack))
            self.stack.clear()
            return self.reverseStack.pop()
        #리버스 스택이 비어있지 않으면 그대로 pop
        else:
            return self.reverseStack.pop()
        
stack = queueStack()

while True:
    print("1. 푸시 2.팝")
    i = int(input())
    if i == 1:
        stack.push(int(input()))
    elif i == 2:
        print(stack.popStack())
    else:
        break
    print(stack.stack)
    print(stack.reverseStack)