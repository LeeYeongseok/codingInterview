import sys

n = 1775

zeroOne = []

count = 0
nowNum = 0

while n != 0:
    if nowNum == n % 2:
        count += 1
    else:
        nowNum = 1 - nowNum
        zeroOne.append(count)
        count = 1
    n >>= 1
zeroOne.append(count)


if len(zeroOne) == 1:
    print(0)
else:
    largeOne = 0
    index = 1
    while index < len(zeroOne):
        largeOne = max(zeroOne[index], largeOne)
        index += 2
    
    index = 2
    while index+1 < len(zeroOne):
        if zeroOne[index] == 1:
            largeOne = max(largeOne, zeroOne[index-1]+zeroOne[index+1]+1)
        index += 2
    print(largeOne)
