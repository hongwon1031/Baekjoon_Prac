import sys
from collections import deque
def input():
    return sys.stdin.readline()
queue = deque([])

def push(x):
    queue.append(x)
def pop():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[0])
        queue.popleft()
def size():
    print(len(queue))
def empty():
    if len(queue) == 0:
        print(1)
    else:
        print(0)
def front():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[0])
def back():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[-1])
        

n = int(input())
for i in range(n):
    a = input().strip()


    if ' ' in a:
        a,b = a.split()
        push(b)
    else:
        if a == 'pop':
            pop()
        elif a == 'size':
            size()
        elif a == 'empty':
            empty()
        elif a == 'front':
            front()
        elif a == 'back':
            back()
    

        