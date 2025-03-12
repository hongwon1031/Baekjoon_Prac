import sys
from collections import deque
def input():
    return sys.stdin.readline()

N = int(input())
a = list(map(int,input().split()))
M = int(input())
b = list(map(int,input().split()))
for i in range(M):
    if b[i] in a:
        print(1,end=' ')
    else:
        print(0,end=' ')