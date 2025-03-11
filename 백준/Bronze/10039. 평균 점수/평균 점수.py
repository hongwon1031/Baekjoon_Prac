import sys
def input():
    return sys.stdin.readline()

li = []
for i in range(5):
    n = int(input())
    if n < 40:
        n = 40
    li.append(n)

print(sum(li)//5)