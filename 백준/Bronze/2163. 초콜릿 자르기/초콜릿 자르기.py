import sys
def input():
    return sys.stdin.readline()
N,M = map(int,input().split())
print((N-1)+(M-1)*(N))

