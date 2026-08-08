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





from collections import defaultdict
import math
def convert(time):
    h,m = time.split(":")
    h,m = int(h), int(m)
    return h * 60 + m
    
def solution(fees, records):
    d_t, d_f, p_t, p_f = fees
    records_dict = dict()
    cumulate_time = defaultdict(int)# 그냥 딕셔너리는 dict(), defaultdict는 defaultdict(int)로 선언하면 됨
    for r in records:
        time, car_num, trigger = r.split(" ")
        cur_time = convert(time)
        if(trigger == "IN"):
            records_dict[car_num] = cur_time
        else:
            prev_time = records_dict.pop(car_num) # popㅇ로 꺼냄 주의
            cumulate_time[car_num] += (cur_time - prev_time)
    if(len(records_dict) != 0):
        for ky, vl in records_dict.items(): # 키 밸류 값 items()로 뽑을 수 있음
            cur_time = convert("23:59")
            cumulate_time[ky] += (cur_time - vl)
    lst = []
    for ky in cumulate_time.keys(): # 키 값만 뽑을 떄는 keys()
        lst.append(ky)
    lst.sort()
    ans = []
    for l in lst:
        car, cum = l, cumulate_time[l]
        if(cum<=d_t):
            ans.append(d_f)
        else:
            ans.append(d_f+math.ceil((cum-d_t)/p_t)*p_f)
    return ans
        
    
            
            
        

