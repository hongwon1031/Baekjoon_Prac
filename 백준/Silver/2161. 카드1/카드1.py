import sys
from collections import deque
def input():
    return sys.stdin.readline()

N = int(input())
li = deque([i+1 for i in range(N)])


new_li = []



while True:
    a = li.popleft()
    new_li.append(a)
    print(a,end=' ')
    li.rotate(-1)

    if len(li) == 0:
        break

