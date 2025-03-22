import sys
def input():
    return sys.stdin.readline()

president = {'Franklin' : 100,'Grant' : 50,'Jackson':20,'Hamilton':10,'Lincoln':5,'Washington':1}

n = int(input())

for _ in range(n):
    a = list(map(str,input().split()))
    sum = 0
    for i in range(len(a)):

        sum += president[a[i]]
    print(f'${sum}')