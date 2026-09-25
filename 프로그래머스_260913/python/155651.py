#호텔대실문제
def convert(tmp):
    start_time, end_time = 0,0
    for i in range(2):
        h, m = tmp[i].split(":")
        time = int(h) * 60 + int(m)
        if(i == 0):
            start_time = time
        else:
            end_time = time
    return (start_time, end_time)
        
        

def solution(book_time):
    book_time.sort()
    room = []
    for b in book_time:
        (start_time, end_time) = convert(b)
        gOrStop = 0
        for r in room:
            if(r <= start_time):
                room.remove(r)
                room.append(end_time + 10)
                gOrStop = 1
                break
        if(gOrStop != 1):
            room.append(end_time + 10)
    return len(room)

#두번쨰 풀이: heapq써서 remove 소요 시간 줄인 버전
# import heapq
# def solution(book_time):
#     book_time.sort()
#     q = []
#     for b in book_time:
#         tmp1, tmp2 = b
#         sh, sm = tmp1.split(":")
#         start_time = int(sh) * 60 + int(sm)
#         eh, em = tmp2.split(":")
#         end_time = int(eh) * 60 + int(em)
#         if(len(q) == 0):
#             heapq.heappush(q, end_time + 10)
#         else:
#             prev_end_time =  heapq.heappop(q)
#             if(prev_end_time <= start_time):
#                 heapq.heappush(q, end_time + 10)
#             else:
#                 heapq.heappush(q, prev_end_time)
#                 heapq.heappush(q, end_time + 10)
#     return len(q)
