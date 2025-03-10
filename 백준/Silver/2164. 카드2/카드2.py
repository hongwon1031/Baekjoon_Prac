import sys
from collections import deque
def input():
    return sys.stdin.readline()
n = int(input())
li = deque([i for i in range(1,n+1)])

while True:
    if len(li) == 1:
        print(li[0])
        break
    li.popleft()
    li.rotate(-1)


