# 지갑의 크기가 30 * 15이고 지폐의 크기가 26 * 17이라면

# 긴쪽을 반으로 접음
# 솔수면 소수점 버림
# 
# wallet = [50, 50]
# bill = [100, 241]

def solution(wallet, bill):
    answer = 0
    while min(bill) > min(wallet) or max(bill) > max(wallet) :
        if bill[0] >= bill[1]:
            bill[0] = int(bill[0] / 2)
        else:
            bill[1] = int(bill[1] / 2)
        answer += 1
    return answer