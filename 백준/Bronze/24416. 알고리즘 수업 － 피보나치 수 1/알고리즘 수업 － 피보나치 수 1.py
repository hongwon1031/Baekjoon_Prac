import sys
def input():
    return sys.stdin.readline()
n = int(input())

def fib(n):
    if n == 1 or n == 2:
        return 1  
    else: 
        return (fib(n - 1) + fib(n - 2))
f = [1,1]
def fibonacci(n):
    count_2 = 0
    for i in range(2,n):
        f.append(f[i-1] + f[i-2])
        count_2 += 1
    return count_2
print(fib(n),fibonacci(n))