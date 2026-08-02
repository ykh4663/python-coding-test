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

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))

    distance[start] = 0

    while q:
        w, fn = heapq.heappop(q)
        if(distance[fn] < w):
            continue
        
        for elem in graph[fn]:
            to, weight = elem # 그래프에서 꺼낼떄는 노드, 가중치 순으로 뽑음
            cost = w + weight
            if(distance[to] > cost):
                distance[to] = cost
                heapq.heappush(q, (cost, to))
    


n, m = map(int, input().split())

start = int(input())

graph = [[] for _ in range(n+1)]

distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

dijkstra(start)
for i in range(1,n+1):
    if(distance[i] < INF):
        print(distance[i])

