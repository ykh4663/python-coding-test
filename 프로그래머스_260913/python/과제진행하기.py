#programmers 176962
from collections import deque
def convert(elem):
    h, m = elem.split(":")
    return int(h) * 60 + int(m)
def solution(plans):
    answer = []
    plans.sort(key = lambda x : x[1])
    q = deque()
    prev_time = convert(plans[0][1])
    answer = []
    for p in plans:
        cur_lang, cur_time, cur_dur = p
        cur_time = convert(cur_time)
        cur_dur = int(cur_dur)
        gap = cur_time - prev_time
        while q:
            if(gap <= 0):
                break
            prev_lang, prev_dur = q.pop()
            if(gap >= prev_dur):
                answer.append(prev_lang)
            else:
                q.append((prev_lang, prev_dur - gap))
            gap -= prev_dur
        q.append((cur_lang, cur_dur))
        prev_time = cur_time
    
    while q:
        l, d = q.pop()
        answer.append(l)
    return answer
                
            
            
    
    
    
    
    return answer