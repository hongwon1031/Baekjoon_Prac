import sys
def input():
    return sys.stdin.readline()

stack = []

def push(x):
    stack.append(x)
def pop():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])
        stack.pop()

def size():
    print(len(stack))

def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)

def peek():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])

dict = {'1' : 'push','2':'pop','3':'size','4':'empty','5':'peek'}
N = int(input())
li = [list(map(int,input().split())) for _ in range(N)]




for i in range(N):
    if li[i][0] == 1:
        push(li[i][1])
    elif li[i][0] == 2:
        pop()
    elif li[i][0] == 3:
        size()
    elif li[i][0] == 4:
        empty()
    elif li[i][0] == 5:
        peek()
    
