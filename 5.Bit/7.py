import sys

def changeOddEven(num):
    return ((num & 0xaaaaaaaa) >> 1 ) | ((num & 0x55555555) << 1)

inputNum = 0b1110010101100110101101
print(bin(inputNum))
print(bin(changeOddEven(inputNum)))