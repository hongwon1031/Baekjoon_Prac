import sys
def input():
    return sys.stdin.readline()
while True:
    a,b = map(int,input().split())
    if (not a) and (not b):
        break

    if b%a == 0:
        print('factor')
    elif a%b == 0:
        print('multiple')
    else:
        print('neither')
    