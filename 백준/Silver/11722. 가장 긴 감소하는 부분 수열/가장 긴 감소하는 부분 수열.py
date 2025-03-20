import sys
def input():
    return sys.stdin.readline()
A = int(input())
li = list(map(int,input().split()))
dp = [1]*A
for i in range(A-2,-1,-1):  #4,3,2,1,0
    for j in range(A-1,i,-1):  #5
        if li[i] > li[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))