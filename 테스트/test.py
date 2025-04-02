import sys
def input():
    return sys.stdin.readline()

li = [int(input()) for _ in range(10)]
sum = li[0] - sum(li[1:])
print(sum)
