import sys
def input():
    return sys.stdin.readline()

# 10초전, 10초후, 오프닝 건너뛰기

# 10초전
# 'prev' 입력시 10초전으로 이동
# 10초 미만이면 처음위치 (0분0초)로 이동

# 10초 후
# 'next' 입력시 10초 후로 이동
# 남은게 10초 미만이면 마지막(영상 길이)로 이동

# 오프닝 건너뒤기
# op_start ≤ 현재 재생 위치 ≤ op_end 이면 자동으로 오프닝 끝나는 위치로 이동
# "10:55", "00:05", "00:15", "06:55", ["prev", "next", "next"]

video_len = '' #동영상 길이
pos = '' # 기능 수행 직전의 재생위치
op_start = '' # 오프닝 시작 시간
op_end = '' # 오프닝이 끝나는 시간
commands = [] # 사용자의 입력


def change(text):
    mm,ss = text.split(':')
    result = int(mm) * 60 + int(ss)
    return result

def rechange(text):
    mm = int(text) // 60
    ss = int(text) % 60
    if mm < 10:
        mm = '0'+str(mm)
    if ss < 10:
        ss = '0'+str(ss)
    result = f'{mm}:{ss}'
    return result



# 사용자 입력이 모두 끝난 후 영상 위치를 'mm:ss' 형식으로 return

def solution(video_len, pos, op_start, op_end, commands):
    video_len,pos,op_start,op_end = change(video_len),change(pos),change(op_start),change(op_end) # 정수변환
    if pos >= op_start and pos <= op_end: # 현 위치가 오프닝 구간일때 
            pos = op_end # 오프닝 스킵
            
    for i in commands: # 입력만큼 반복
        #next
        if i == 'next':
            pos += 10
            if pos > video_len:
                pos = video_len
            print('next',pos)
            
        elif i == 'prev':
            pos -= 10
            if pos < 0:
                pos = 0
            print('prev',pos)
            
        if pos >= op_start and pos <= op_end: # 현 위치가 오프닝 구간일때 
            pos = op_end # 오프닝 스킵
            
    answer = rechange(pos)
    return answer