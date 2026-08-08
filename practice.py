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

from collections import defaultdict
def solution(want, number, discount):
    dct = defaultdict(int)
    cum_len = 10
    for i in range(len(want)):
        dct[want[i]] = number[i]
    dlen = len(discount)
    total = 0
    
    # 0 1 2 3 4 5   6 - 3 = 3
    # 0 1 2
    
    for i in range(dlen-cum_len+1):
        tmp = defaultdict(int)
        for j in range(cum_len):
            tmp[discount[i+j]] +=1
        gOrStop = 0
        
        for key in tmp.keys():
            if key not in dct.keys():
                gOrStop = 1
                break
            if(tmp[key] != dct[key]):
                gOrStop = 1
                break
        if(gOrStop == 0):
            total+=1

                
    return total  
        
        


want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
result = solution(want, number, discount)
print(result)


