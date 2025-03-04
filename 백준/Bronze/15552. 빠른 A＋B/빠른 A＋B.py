import sys
n = sys.stdin.readline()


for i in range(int(n)):
    a = sys.stdin.readline().rstrip()
    a,b = a.split(' ')
    print(int(a)+int(b))