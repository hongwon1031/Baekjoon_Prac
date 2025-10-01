import math
def solution(n):
    result = math.sqrt(n)
    if str(result)[-1] == '0':
        return int((result + 1)**2)
    else:
        return -1