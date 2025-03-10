import sys
def input():
    return sys.stdin.readline()

first = input().strip()
second = input().strip()
third = input().strip()

next = 0

if first.isdigit():
    next = int(first) + 3

elif second.isdigit():
    next = int(second) + 2
elif third.isdigit():
    next = int(third) + 1




if (next%3 == 0) and (next%5 == 0):   #15,30,45
    print('FizzBuzz')
elif (next%3 == 0) and (next%5 != 0): # 3,6,9,12,18
    print('Fizz')
elif (next%3 != 0) and (next%5 == 0): # 5,10,20
    print('Buzz')
else:
    print(next)


