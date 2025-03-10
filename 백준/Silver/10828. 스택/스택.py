import sys
stack = []
def input():
    return sys.stdin.readline()
def push(x):
    stack.append(x)
def top():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])
def pop():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])
        del stack[-1]
def size():
    print(len(stack))
def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)
n = int(input())
li = [list(map(str,input().split())) for _ in range(n)]


for i in range(n):

    
    if li[i][0] == 'push':
        push(li[i][1])
    elif li[i][0] == 'top':
        top()
    elif li[i][0] == 'size':
        size()
    elif li[i][0] == 'empty':
        empty()
    elif li[i][0] == 'pop':
        pop()

        

