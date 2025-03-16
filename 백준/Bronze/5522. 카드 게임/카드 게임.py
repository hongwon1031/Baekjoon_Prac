import sys
def input():
    return sys.stdin.readline()

sum = 0
for _ in range(5):
    a = int(input())
    sum += a
print(sum)