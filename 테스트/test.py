import sys
def input():
    return sys.stdin.readline()
n,b = map(str,input().split())
print(n,b)
dict = {}
for i in range(1,10):
    dict[i] = i
'''for i in range(10,36):
    
sum = 0
for i in range(len(n)-1,-1,-1):
    j = 0
    sum += (n[i]**j) * int(b)
    print(sum)
    print('j=',j)
    j += 1
print(sum)'''
print(ord('Z'))