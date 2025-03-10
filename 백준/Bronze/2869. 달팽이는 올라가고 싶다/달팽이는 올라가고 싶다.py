import sys
import math
def input():
    return sys.stdin.readline()
A,B,V = map(int,input().split(' '))

print(math.ceil((V-A)/(A-B))+1)

