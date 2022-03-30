from operator import xor
import sys

a = 29 #11101
b = 15 #01111

c = a ^ b
count = 0
while c > 0:
    if c%2 == 1:
        count += 1
    c>>=1

print(count)