def solution(n):
    for i in range(1,n+1):
        answer = 0
        if n % i == 1:
            answer = i
            break
    return answer