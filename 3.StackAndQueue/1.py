import sys

stack = []
first, second, third = 0, 0, 0
def insert(i, n):
    global first, second, third, stack
    if i == 1:
        stack.insert(first, n)
        first += 1
        second += 1
        third += 1
    elif i == 2:
        stack.insert(second,n)
        second += 1
        third += 1
    elif i == 3:
        stack.insert(third,n)
        third += 1
    else:
        print("유효하지 않은 스택")

def pop(i):
    global first, second, third, stack
    ans = 0
    if i == 1:
        if first == 0:
            return "없음"
        ans = stack.pop(first-1)
        first -= 1
        second -= 1
        third -= 1
    elif i == 2:
        if second - first == 0:
            return "없음"
        ans = stack.pop(second-1)
        second -= 1
        third -= 1
    elif i == 3:
        if third - second == 0:
            return "없음"
        ans = stack.pop(third-1)
        third -= 1
    else:
        print("유효하지 않은 스택")
        return
    return ans

while True:
    choose = input()
    
    if choose == 'push':
        i, n = map(int, input().split())
        insert(i, n)
    elif choose == 'pop':
        i = int(input())
        print(pop(i))
    else:
        break