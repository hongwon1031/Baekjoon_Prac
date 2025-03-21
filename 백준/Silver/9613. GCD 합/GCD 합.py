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
    li = list(map(int,input().split()))
    sum = 0
    for i in range(1,li[0]+1):  #1234
        for j in range(i+1,li[0]+1):#234
            sum += gcd(li[i],li[j])            
    print(sum)
