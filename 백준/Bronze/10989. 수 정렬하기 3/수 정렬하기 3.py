import sys

def input():
    return sys.stdin.readline()
N = int(input())

count = [0] * 10001

for _ in range(N):
    a = int(input())
    count[a] += 1

for i in range(10001):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)