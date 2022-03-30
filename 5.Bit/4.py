from cgitb import small
import sys

num = 0b10110010

count = 0
while num > 0:
    if num % 2 == 0:
        count += 1
    num >>= 1
largeNum = '0b' + '1'*count + '0'*(32-count)
smallNum = '0b' + '0'*(32-count) + '1'*count

print(largeNum)
print(smallNum)
print(int(largeNum, 2))
print(int(smallNum, 2))