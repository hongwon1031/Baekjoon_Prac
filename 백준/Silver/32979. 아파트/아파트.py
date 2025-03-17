import sys
from collections import deque
def input():
    return sys.stdin.readline()
N = int(input())
T = int(input())
a = deque(list(map(int,input().split())))
b = list(map(int,input().split()))

for j in range(T):
    for _ in range(b[j]-1):
        a.rotate(-1)
    print(a[0],end=' ')