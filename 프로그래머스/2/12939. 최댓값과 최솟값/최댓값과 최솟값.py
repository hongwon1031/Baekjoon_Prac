def solution(s):
    answer = [0,0]
    a = str(min(list(map(int,s.split(' ')))))
    b = str(max(list(map(int,s.split(' ')))))
    return '{} {}'.format(a,b)