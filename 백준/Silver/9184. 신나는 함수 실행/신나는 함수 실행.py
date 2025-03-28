import sys
import math

def input():
    return sys.stdin.readline()
dp = {}

def w(a,b,c):
    
    if (a,b,c) in dp:
        result = dp[(a,b,c)]
    else:
        if a <= 0 or b <= 0 or c <= 0:
            #a,b,c중 하나라도 음수라면
            result = 1

        elif a > 20 or b > 20 or c > 20:
            #a,b,c중 하나라도 20보다 크다면
            
            result = w(20, 20, 20)

        elif a < b and b < c:
            
            result = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

        else :
            result = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        
        dp[(a,b,c)] = result

    return result

while True:
    a,b,c = map(int,input().split())
    if a == -1 and b == -1 and c == -1:
        break
    else:
        print(f'w({a}, {b}, {c}) = {w(a,b,c)}')
