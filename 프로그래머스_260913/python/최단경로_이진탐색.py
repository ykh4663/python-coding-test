#떡볶이 떡 만들기
# n, m = map(int, input().split())
# lst = list(map(int, input().split()))
# lst.sort(reverse = True)
# l, r = 0, lst[0]
# answer = 0
# while(l <= r):
#     mid = (l+r) // 2
#     cnt = 0
#     for li in lst:
#         if(li > mid):
#             cnt+=(li - mid)
#         else:
#             break
#     if(cnt >= m):
#         print(answer)
#         answer = max(answer, mid)
#         l = mid+1
#     else:
#         r = mid-1
# print(answer)

#전보
import heapq
INF = int(1e9)

def dijkstra(graph, distance, start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        weight, node = heapq.heappop(q)
        if(weight > distance[node]):
            continue
        for g in graph[node]:
            nd, wg = g
            w = weight + wg
            if(w < distance[nd]):
                heapq.heappush(q, (w, nd))
                distance[nd] = w
    

n,m,c = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x,y,z = map(int, input().split())
    graph[x].append((y,z))


distance = [INF] * (n+1)
dijkstra(graph, distance, c)
mx = 0
cnt = 0
for i in range(1, n+1):
    if(distance[i] == INF or i == c):
        continue
    else:
        cnt+=1
        mx = max(mx, distance[i])
print(cnt, mx)




