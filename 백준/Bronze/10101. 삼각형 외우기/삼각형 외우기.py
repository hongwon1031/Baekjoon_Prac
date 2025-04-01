import sys
def input():
    return sys.stdin.readline()
li = [int(input()) for _ in range(3)]
if li[0] == 60 and li[1] == 60 and li[2] == 60:
    result = 'Equilateral'
elif sum(li) == 180 :
    if li[0] == li[1] or li[1] == li[2] or li[2] == li[0]:
        result = 'Isosceles'
    else:
        result = 'Scalene'
else:
    result = 'Error'
print(result)