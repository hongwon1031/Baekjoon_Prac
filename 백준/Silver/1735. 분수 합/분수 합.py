import sys

def gcd(a,b):   #최대공약수

    while b>0:
        a,b = b,a%b
    return a

def input():
    return sys.stdin.readline()

def lcm(a,b):   #최소공배수
    return a*b/gcd(a,b)

a1,a2 = map(int,input().split())
b1,b2 = map(int,input().split())
result_lcm = lcm(a2,b2)

a1,b1 = int((result_lcm/a2)*a1),int((result_lcm/b2)*b1)
result_2 = int(result_lcm)
result_1 = a1+b1

result_gcd_2 = gcd(result_1,result_2)
result_1 /= result_gcd_2
result_2 /= result_gcd_2
print(int(result_1),int(result_2))