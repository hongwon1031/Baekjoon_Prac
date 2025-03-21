import sys
def input():
    return sys.stdin.readline()

N,K = map(int,input().split())

li = [k+1 for k in range(N)]
i = 0
print(end='<')

for _ in range(N):
    i += K-1
    if i >= len(li):
        i = i%len(li)

    if len(li) == 1:
        print(li[i],end='>') 
        li.remove(li[i])   
    else:
        
        
        print(li[i],end=', ')
        li.remove(li[i])
    



