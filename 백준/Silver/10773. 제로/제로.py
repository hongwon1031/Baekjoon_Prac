import sys
def input():
    return sys.stdin.readline()
K = int(input())
li = []
for i in range(K):
    a = int(input())
    if a == 0:
        li.pop()
    else:
        li.append(a)
print(sum(li))
