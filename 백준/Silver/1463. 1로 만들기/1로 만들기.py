import sys

def input():
    return sys.stdin.readline()

count = 0
n = int(input())
dp = [-1] + [0,1,1] + [-1]*(n-3)


for i in range(4,n+1):
    if i % 3 == 0 and i % 2 == 0:
        dp[i] = min(dp[i-1],dp[i//2],dp[i//3]) + 1
    elif i % 2 == 0:
        dp[i] = min(dp[i-1],dp[i//2]) + 1
    elif i % 3 == 0:
        dp[i] = min(dp[i-1],dp[i//3]) + 1
    else:
        dp[i] = dp[i-1] + 1
print(dp[n])