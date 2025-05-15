# t초동안 1초마다 x만큼 회복
# t초 연속 성공 -> +y
# 최대 체력 존재
# 공격당하면 기술 취소, 순간에는 회복 불가
# bandage : 붕대감기 시전시간, 초당 회복량, 추가 회복량
# health : 최대 체력
# attacks : 몬스터 공격시간, 피해량
from collections import deque
import sys
def input():
    return sys.stdin.readline()


def solution(bandage, health, attacks):
    attacks = deque(attacks)
    hp = health # hp
    time_len = attacks[-1][0] # 11
    bandage_count = 0 #붕대카운트 초기화
    
    for i in range(1,time_len + 1):
        # 몬스터 공격 o
        if i == attacks[0][0]:
            # 붕대 초기화
            hp -= attacks[0][1]
            bandage_count = 0 # 초기화
            attacks.popleft() # 삭제
        
        # 몬스터 공격 x
        else:
            # 붕대 감기
            hp += bandage[1]
            # 최대체력일때
            if hp > health:
                hp = health
            # 붕대 카운트 증가
            bandage_count += 1
                # 카운트 넘기면 추가체력
            if bandage_count >= bandage[0]:
                bandage_count = 0
                hp += bandage[2]
                if hp > health:
                    hp = health
        if hp <= 0:
            hp = -1
            break
    answer = hp
    return answer