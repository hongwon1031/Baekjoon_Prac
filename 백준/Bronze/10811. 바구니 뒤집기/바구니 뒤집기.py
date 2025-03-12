
import sys
def input():
    return sys.stdin.readline()
N,M = map(int,input().split()) # 5,4
li = [i+1 for i in range(N)] # 12345

for i in range(M):
    a,b = map(int,input().split())  #1 2
    mid = (a+b)//2    # 2
    
    while a <= mid: #1 < 2
        n = li[b-1] # 
        li[b-1] = li[a-1]
        
        li[a-1] = n
        
        a += 1
        b -= 1
for i in li:
    print(i,end=' ')        


