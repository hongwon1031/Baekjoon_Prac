import math
import sys
def input():
    return sys.stdin.readline()

N,K = map(int,input().split())

li = [True for i in range(N+1)]    #01234567
count = 0
li[0] = False
li[1] = False
result = 0

for i in range(2,N+1):  #2~4
    if li[i] == True:
        for j in range(i,N+1,i):  #4~7 2씩
            if li[j]:
                li[j] = False
                count+=1
                if count == K:
                    result = j
                    break
print(result)


