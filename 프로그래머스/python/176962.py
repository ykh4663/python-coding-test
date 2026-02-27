from collections import deque

def convert(elem):
    hour, minute = map(int, elem.split(":"))
    return hour * 60 + minute

def solution(plans):
    plans.sort(key=lambda x : x[1])
    p_len = len(plans)
    q = deque()
    result = []
    for i in range(p_len):
        plans[i][1] = convert(plans[i][1])
        plans[i][2] = int(plans[i][2])
    for i in range(p_len-1):
        name, start_time, lasts = plans[i]
        next_start_time = plans[i+1][1]
        if(start_time + lasts <= next_start_time):#다음 시작 시간 내에 끝나는 케이스
            result.append(name)
            remain_time = next_start_time - (start_time+lasts)
            while(len(q) != 0 and remain_time > 0):
                q_name, q_time = q.pop()
                if(q_time <= remain_time):
                    result.append(q_name)
                    remain_time -= q_time
                else:
                    q.append((q_name, q_time - remain_time))
                    break
        else:#다음 시작시간 내에 끝나지 못하는 케이스
            q_time = lasts - (next_start_time - start_time)
            q.append((name, q_time))
    result.append(plans[-1][0])
    while(q):
        q_name, q_time = q.pop()
        result.append(q_name)
    return result
            
            
            
            
    