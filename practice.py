# import sys
# input = sys.stdin.readline
# INF = int(1e9)

# def get_smallest_node():
#     small = INF
#     small_idx = 0
#     for i in range(1,n+1):
#         if(small > distance[i] and visited[i] == False):
#             small = distance[i]
#             small_idx = i
#     return small_idx

# def dijkstra(start):
#     distance[start] = 0
#     # for elem in graph[start]:
#     #     t,w = elem
#     #     distance[t] = w
    
#     for i in range(n):
#         idx = get_smallest_node()
#         visited[idx] = True
#         for elem in graph[idx]:
#             to, weight = elem
#             distance[to] = min(distance[to], distance[idx] + weight)



# n, m = map(int, input().split())

# start = int(input())

# graph = [[] for _ in range(n+1)]
# visited = [False] * (n+1)
# distance = [INF] * (n+1)
# for i in range(m):
#     f, t, w = map(int, input().split())
#     graph[f].append((t,w))

# dijkstra(start)
# for i in range(1,n+1):
#     if(distance[i] != INF):
#         print(distance[i])

# ver2
# import sys
# import heapq
# input = sys.stdin.readline
# INF = int(1e9)


# def dijkstra(start):
#     q = []
#     heapq.heappush(q, (0,start))

#     distance[start] = 0

#     while q:
#         w, fn = heapq.heappop(q)
#         if(distance[fn] < w):
#             continue
        
#         for elem in graph[fn]:
#             to, weight = elem # 그래프에서 꺼낼떄는 노드, 가중치 순으로 뽑음
#             cost = w + weight
#             if(distance[to] > cost):
#                 distance[to] = cost
#                 heapq.heappush(q, (cost, to))
    


# n, m = map(int, input().split())

# start = int(input())

# graph = [[] for _ in range(n+1)]

# distance = [INF] * (n+1)

# for _ in range(m):
#     a,b,c = map(int, input().split())
#     graph[a].append((b,c))

# dijkstra(start)
# for i in range(1,n+1):
#     if(distance[i] < INF):
#         print(distance[i])




# def solution(s):
#     slen = len(s)
#     answer = slen

#     for i in range(1, slen // 2+1):
#         local_ans = ""
#         tmp = s[:i]
#         cnt = 1
#         for j in range(i, slen, i):
#             if(tmp == s[j:j+i]):
#                 cnt+=1
#             else:
#                 if(cnt > 1):
#                     local_ans += str(cnt)
#                 local_ans += tmp
#                 tmp = s[j:j+i]
#                 cnt = 1
#         if(cnt > 1):
#             local_ans += str(cnt)
#         local_ans += tmp
#         answer = min(answer, len(local_ans))


#     return answer


# s = "xababcdcdababcdcd"
# print(solution(s))


# from collections import deque

# def solution(s):
    
#     slen = len(s)
#     total = 0
#     for x in range(len(s)):
#         q = deque()
#         s_rotate_x = s[x:] + s[:x]
#         gOrStop = 0
#         for i in range(slen):
#             cur = s_rotate_x[i] 
#             if(cur == '[' or cur == '{' or cur == '('):
#                 q.append(cur)
#             else:
#                 if(len(q) == 0):
#                     gOrStop = 1
#                     break
#                 prev = q.pop()
#                 if((prev == '[' and cur == ']') or (prev == '{' and cur == '}') or (prev == '(' and cur == ')')):
#                     continue
#                 else:
#                     gOrStop = 1
#                     break
#         if(len(q) != 0):
#             gOrStop = 1
#         if(gOrStop == 0):
#             total +=1
#     return total

                




# def convert(n, k):
#     lst = []
#     while(n > 0):
#         lst.append(str(n % k))
#         n //= k
#     lst.reverse()
#     return ''.join(lst)

# def isPrime(elem):
#     if(elem < 2):
#         return False
#     for i in range(2, int(elem **0.5) + 1):
#         if(elem % i == 0):
#             return False
#     return True


# def solution(n, k):
#     elem = convert(n,k)
#     prev = 0
#     cnt = 0
#     tmp = 0
#     for i in range(len(elem)):
#         if(elem[i] == '0'):
#             if(prev != i):
#                 tmp = int(elem[prev:i])
#                 if(isPrime(tmp) == True):
#                     cnt+=1
#             prev = i+1
#     if(prev != len(elem)):
#         if(isPrime(int(elem[prev:len(elem)])) == True):
#             cnt+=1
        
            

#     return cnt


# n = 437674
# k = 3
# print(solution(n, k))


#92341_programmers_주차요금계산하기
# from collections import defaultdict
# import math

# def convert(elem):
#     time = elem.split(":")
#     hour = int(time[0])
#     minute = int(time[1])
#     return hour * 60 + minute

# def solution(fees, records):
#     default_time = fees[0]
#     default_fee = fees[1]
#     per_time = fees[2]
#     per_fee = fees[3]

#     car_dict = dict()
#     total = defaultdict(int)

#     for record in records:
#         r = record.split(" ")
#         str_time = r[0]
#         car_num = r[1]
#         iout = r[2]
#         cur = convert(str_time)
#         if(iout == "IN"):
#             car_dict[car_num] = cur

#         else:
#             prev = car_dict.pop(car_num)
#             total[car_num] += (cur - prev)
    
#     for ky, prev in car_dict.items():
#         cur = convert("23:59")
#         total[ky] += (cur - prev)
    

#     lst = list(total.keys())
#     lst.sort()

#     answer = []
#     for cn in lst:
#         if(total[cn] <= default_time):
#             answer.append(default_fee)
#         else:
#             answer.append( default_fee + math.ceil((total[cn] - default_time) / per_time) * per_fee )
    

#     return answer



    



            
# fees = [180, 5000, 10, 600]
# records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
# result = solution(fees, records)
# print(result)


#131127_programmers_할인행사

# from collections import defaultdict
# def solution(want, number, discount):
#     dct = defaultdict(int)
#     cum_len = 10
#     for i in range(len(want)):
#         dct[want[i]] = number[i]
#     dlen = len(discount)
#     total = 0
    
#     # 0 1 2 3 4 5   6 - 3 = 3
#     # 0 1 2
    
#     for i in range(dlen-cum_len+1):
#         tmp = defaultdict(int)
#         for j in range(cum_len):
#             tmp[discount[i+j]] +=1
#         gOrStop = 0
        
#         for key in tmp.keys():
#             if key not in dct.keys():
#                 gOrStop = 1
#                 break
#             if(tmp[key] != dct[key]):
#                 gOrStop = 1
#                 break
#         if(gOrStop == 0):
#             total+=1

                
#     return total  
        
        


# want = ["banana", "apple", "rice", "pork", "pot"]
# number = [3, 2, 2, 2, 1]
# discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
# result = solution(want, number, discount)
# print(result)



# number = 13195
# max_div = 0
# for i in range(2,number):
#     if(isPrime(i) and number % i == 0):
        
# from itertools import combinations
# from collections import deque
# import copy

# dx = [1,-1,0,0]
# dy = [0,0,1,-1]

# def bfs(graph, sx, sy, n, m):
#     q = deque()
#     q.append((sx, sy))
#     graph[sx][sy] = 3
#     while q:
#         x,y = q.popleft()
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if(0<=nx<n and  0<=ny<m):
#                 if(graph[nx][ny]== 0 or graph[nx][ny] == 2):
#                     graph[nx][ny] = 3
#                     q.append((nx, ny))

# def findSafe(graph, n, m):
#     cnt = 0
#     for i in range(n):
#         for j in range(m):
#             if(graph[i][j] == 0):
#                 cnt+=1
#     return cnt
    


# n,m = map(int, input().split())
# lst = []
# for _ in range(n):
#     lst.append(list(map(int, input().split())))

# comb = []
# for i in range(n):
#     for j in range(m):
#         if(lst[i][j] == 0):
#             comb.append((i,j))
# comb = list(combinations(comb, 3))
# total = 0
# for c in comb:
#     graph = copy.deepcopy(lst)
#     (x1, y1), (x2, y2), (x3, y3) = c
#     graph[x1][y1] = graph[x2][y2] = graph[x3][y3] = 1
#     for i in range(n):
#         for j in range(m):
#             if(graph[i][j] == 2):
#                 bfs(graph, i, j, n, m)
    
#     total = max(total, findSafe(graph, n, m))
# print(total)

            
# from collections import defaultdict
# import math
# def convert(time):
#     h,m = time.split(":")
#     return int(h) * 60 + int(m)

# def solution(fees, records):
#     default_time, default_fee, per_time, per_fee = fees
#     answer = []
#     tmp = dict()
#     dct = defaultdict(int)
#     for r in records:
#         t, cn, trigger = r.split(" ")
#         cur_time = convert(t)
#         if(trigger == "IN"):
#             tmp[cn] = cur_time
#         else:
#             prev_time = tmp.pop(cn)
#             dct[cn] += (cur_time - prev_time) 
#     if(len(tmp) != 0):
#         for car_number, prev_time in tmp.items():
#             cur_time = convert("23:59")
#             dct[car_number] += (cur_time - prev_time)
#     lst = [i for i in dct.keys()]
#     lst.sort()
    
#     for l in lst:
#         time = dct[l]
#         if(time <= default_time):
#             answer.append(default_fee)
#         else:
#             answer.append(default_fee + math.ceil((time - default_time) / per_time) * per_fee)
        

    
    
#     return answer


# from collections import deque

# def convert(elem):
#     h, m = elem.split(":")
#     return int(h) * 60 + int(m)

# def solution(plans):
#     q = deque()
#     plans.sort(key = lambda x : x[1])
#     plen = len(plans)
#     last_time = 0
#     result = []
#     for i in range(plen):
#         language, time, duration = plans[i]
#         t = convert(time)
#         time = t
#         duration = int(duration)
#         while q:
#             prev_lang, prev_time, prev_dur = q.pop()
#             if(time - prev_time >= prev_dur):
#                 result.append(prev_lang)
#                 time -= prev_dur
#                 print(prev_lang, prev_dur)
#             else:
#                 q.append((prev_lang, prev_time, prev_dur - (time-prev_time)))
#                 break
#         q.append((language, t, duration))
#     while q:
#         l, t, d = q.pop()
#         result.append(l)
#     return result
                
                
            

# plans = [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]
# result = solution(plans)
# print(result)



# from collections import deque
# dx = [1,-1,0,0]
# dy = [0,0,1,-1]

# def bfs(graph, s, e, n, m):
#     visit = [[False] * m for _ in range(n)]
#     q = deque()
#     (sx, sy) = s
#     (ex, ey) = e

#     q.append((0, sx, sy))
#     visit[sx][sy] = True
#     while q:
#         (weight, x, y) = q.popleft()
#         if(x == ex and y == ey):
#             return weight
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if(0<=nx<n and 0<=ny<m):
#                 if(visit[nx][ny] == False and graph[nx][ny] != 'X'):
#                     visit[nx][ny] = True
#                     q.append((weight+1, nx, ny))
#     return -1
    
    
    
    
# def solution(maps):

#     r, c = len(maps), len(maps[0])
    
#     s,e,labber = 0,0, 0
#     cnt = 0
#     for i in range(r):
#         for j in range(c):
#             if(maps[i][j] == 'S'):
#                 s = (i,j)
#                 cnt+=1
#             elif(maps[i][j] == 'E'):
#                 e = (i,j)
#                 cnt+=1
#             elif(maps[i][j] == 'L'):
#                 labber = (i,j)
#                 cnt+=1
#             if(cnt == 3):
#                 break
#         if(cnt == 3):
#             break
#     e1 = bfs(maps, s,labber, r, c)
#     if(e1 == -1):
#         return -1
#     e2 = bfs(maps, labber, e, r, c)
#     if(e2 == -1):
#         return -1
    
#     answer = e1 + e2        
#     return answer
# maps = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]
# result = solution(maps)
# print(result)

# import sys
# input = sys.stdin.readline
# #k진수에서 소수 개수 구하기 2022 KAKAO BLIND RECRUITMENT
# #게임 맵 최단거리
# #N으로 표현 dp
# MX = 8

# def solution(N, number):
#     dp = [set() for _ in range(MX+1)]
#     for i in range(1,MX+1):
#         rs = 0
#         for j in range(i):
#             rs = rs * 10 + N
#         dp[i].add(rs)
#         for j in range(1,i):
#             for x in dp[j]:
#                 for y in dp[i-j]:
#                     dp[i].add(x+y)
#                     dp[i].add(x-y)
#                     dp[i].add(y-x)
#                     dp[i].add(x*y)
#                     if(x != 0):
#                         dp[i].add(int(y/x))
#                     if(y != 0):
#                         dp[i].add(int(x/y))
#         if number in dp[i]:
#             return i
#     return -1

# from collections import deque
# import copy
# from itertools import combinations

# dx = [1,-1,0,0]
# dy = [0,0,1,-1]


# def bfs(graph, visit, sx, sy, n, m):
#     q = deque()
#     q.append((sx, sy))
#     visit[sx][sy] = True
#     while q:
#         x,y = q.popleft()
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if(0<=nx<n and 0<=ny<m):
#                 if(graph[nx][ny] != 1 and visit[nx][ny] == False):
#                     graph[nx][ny] = 2
#                     visit[nx][ny] = True
#                     q.append((nx, ny))

# def safeArea(graph, n, m):
#     cnt = 0
#     for i in range(n):
#         for j in range(m):
#             if(graph[i][j] == 0):
#                 cnt+=1
#     return cnt



# n,m = map(int, input().split())
# lst = [[0] * m for _ in range(n)]

# comb = []

# for i in range(n):
#     elem = list(map(int, input().split()))
#     for j in range(m):
#         lst[i][j] = elem[j]
#         if(elem[j] == 0):
#             comb.append((i,j))


# comb = list(combinations(comb, 3))
# cnt = -1
# for c in comb:
#     visit = [[False] * m for _ in range(n)]
#     tmp = copy.deepcopy(lst)
#     (x1,y1), (x2,y2), (x3,y3) = c
#     tmp[x1][y1] = tmp[x2][y2] = tmp[x3][y3] = 1
#     for i in range(n):
#         for j in range(m):
#             if(tmp[i][j] == 2 and visit[i][j] == False):
#                 bfs(tmp, visit, i, j, n, m)
#     cnt = max(safeArea(tmp, n, m), cnt)
# print(cnt)





# from collections import deque

# def isPush(elem):
#     if(elem == '{' or elem == '[' or elem == '('):
#         return True
#     return False

# def isPair(prev, cur):
#     if((prev == '(' and cur == ')') or (prev == '{' and cur == '}') or (prev == '[' and cur == ']')):
#         return True
#     return False
    
    
    
# def solution(s):
#     slen = len(s)
#     cnt = 0
#     for i in range(slen):
#         tmp = ""
#         gOrStop = 0
#         tmp += s[i:slen]
#         tmp += s[:i]
#         print(tmp)
#         q = deque()
#         for j in range(slen):
#             cur = tmp[j]
#             if(isPush(cur)):
#                 q.append(cur)
#             else:
#                 if(len(q) == 0):
#                     gOrStop = 1
#                     break
#                 prev = q.pop()
#                 if(isPair(prev, cur)):
#                     continue
#                 else:
#                     gOrStop = 1
#                     break
            
#         if(len(q) != 0):
#             gOrStop = 1
#         if(gOrStop == 0):
#             cnt+=1
            
#     return cnt

# s = "[](){}"
# print(solution(s))

    



# def convert(n, k):
#     lst = []
#     while(n > 0):
#         lst.append(str(n % k))
#         n //= k
#     lst.reverse()
#     return "".join(lst)
    
# def isPrime(elem):
#     if(elem < 2):
#         return 0
#     for i in range(2, int(elem ** 0.5) + 1):
#         if(elem % i == 0):
#             return 0
#     return 1
    
# def solution(n, k):

    
#     elem = convert(n,k)
    
#     l = len(elem)
#     prev = 0
#     cnt = 0
#     for i in range(l):
#         if(elem[i] == '0'):
#             if(prev != i):
#                 cnt+=isPrime(int(elem[prev:i]))
#             prev = i
#     if(prev != l-1):
#         cnt+=isPrime(int(elem[prev:l]))
        
    
    
#     return cnt
# n = 437674
# k = 3
# print(solution(n,k))


# import heapq
# def convert(elem):
#     h,m = elem.split(":")
#     return int(h) * 60 + int(m)
# def solution(book_time):
#     answer = 0
#     q_lst = []
#     book_time.sort()
#     blen = len(book_time)

#     q_lst = [[] for _ in range(blen)]
#     idx = 0
#     for b in book_time:
#         start, end = b
#         cur_start, cur_end = convert(start), convert(end)
#         gOrStop = 0
#         if(idx != 0):
#             for i in range(idx):
#                 if(len(q_lst[i]) != 0):
#                     prev_end = heapq.heappop(q_lst[i])
#                     if(prev_end <= cur_start):
#                         heapq.heappush(q_lst[i], cur_end + 10)
#                         gOrStop = 1
#                         break
#                     else:
#                         heapq.heappush(q_lst[i], prev_end)
#         if(gOrStop == 0):
#             heapq.heappush(q_lst[idx], cur_end+10)
#             idx+=1

            
                    
        
        
            
    
#     return idx

# book_time = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
# result = solution(book_time)
# print(result)

from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(graph, sx, sy, ex, ey, n, m):
    q = deque()
    q.append((0, sx, sy))
    graph[sx][sy] = 'X'
    while q:
        w, x, y = q.popleft()
        if(x == ex and y == ey):
            return w
        for k in range(4):
            nx, ny = x, y
            while(0<=nx<n and 0<=ny<m):
                if(graph[nx][ny] != 'D'):
                    nx+=dx[k]
                    ny+=dy[k]
                else:
                    break
            nx -= dx[k]
            ny -= dy[k]
            if(graph[nx][ny] == 'X'):
                continue
            q.append((w+1, nx, ny))
            graph[nx][ny] = 'X'
    return -1
            
            
    

def solution(board):
    answer = 0
    
    r = len(board)
    c = len(board[0])
    graph = []
    for i in range(r):
        graph.append(list(s for s in board[i]))

    cnt = 0
    sx, sy, ex, ey = 0,0,0,0
    for i in range(r):
        for j in range(c):
            if(graph[i][j] == 'R'):
                cnt+=1
                sx, sy = i,j
            elif(graph[i][j] == 'G'):
                cnt+=1
                ex, ey = i,j
            if(cnt == 2):
                break
        if(cnt == 2):
            break
    return bfs(graph, sx, sy, ex, ey, r, c)
board = [".D.R", "....", ".G..", "...D"]
result = solution(board)
print(result)