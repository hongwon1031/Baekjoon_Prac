import sys

def gcd(a,b):
    if a<b:
        a,b = b,a
    while b>0:
        a,b = b,a%b
    return a

def input():
    return sys.stdin.readline()
n = int(input())
for _ in range(n):
    a,b = map(int,input().split())
    print(gcd(a,b))