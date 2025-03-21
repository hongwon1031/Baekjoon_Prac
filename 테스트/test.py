import sys

def gcd(a,b):   #최대공약수
    while b>0:
        a,b = b,a%b
    return a

def input():
    return sys.stdin.readline()

a,b = map(int,input().split())
def old_gcd(a,b):
    count = 0
    while a!=b:
        a, b = max(a,b) - min(a,b), min(a,b)
        count += 1
    return count
print(old_gcd(a,b))