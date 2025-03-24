import sys
import math

def input():
    return sys.stdin.readline()

dp = [[]]


n = int(input())
dp = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    li = list(map(int,input().split())) # li = 0
    for j in range(i+1): # 0,0

        if i == 0:
            dp[i][j] = li[0]
        elif j == 0 : # i = 1, j = 0
            dp[i][j] = (dp[i-1][j] + li[j])
        elif j == i:
            dp[i][j] = (dp[i-1][j-1] + li[j])
        else:
            dp[i][j] = (max(dp[i-1][j-1],dp[i-1][j]) + li[j])

    
print(max(dp[n-1]))

        