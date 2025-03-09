import sys

def input():
    return sys.stdin.readline()

stack = []
def push(x):
    stack.append(x)
def pop():
    print(stack[-1])
    stack.pop()
def size():
    print(len(stack))

def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)
def top():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])
push(1)
print(stack)
push(2)
print(stack)
top()
print(stack)
size()
print(stack)
empty()
print(stack)
pop()
print(stack)
pop()
print(stack)
pop
print(stack)


'''N = int(input())

for i in range(N):
    a = input()'''
