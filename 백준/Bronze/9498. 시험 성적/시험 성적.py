a = int(input())
def zz(a):
    if (a >= 90) and (a <= 100):
        result = 'A'
    elif (a >= 80) and (a <= 89):
        result = 'B'
    elif (a >= 70) and (a <= 79):
        result = 'C'
    elif (a >= 60) and (a <= 69):
        result = 'D'
    else:
        result = 'F'
    return result
print(zz(a))