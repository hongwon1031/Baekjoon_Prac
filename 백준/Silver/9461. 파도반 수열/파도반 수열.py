import sys
import math
def input():
    return sys.stdin.readline()

dp = [0] * 100
dp[:4] = [1,1,1,2,2]
N = int(input())

def cal(x): #6번째
    x -= 1  #5
    if x <= 2:
        return 1
    elif 2<x<5:
        return 2
    elif dp[x] != 0:
        return dp[x]
    else:
        dp[x] = cal(x-4) + cal(x)
        return dp[x]
for _ in range(N):
    a = int(input())
    print(cal(a))