import heapq
INF = int(1e9)

def dijkstra(graph, start):
    global n
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        w, nd = heapq.heappop(q)
        if(distance[nd] < w):
            continue
        for g in graph[nd]:
            nn, gg = g
            new_g = w + gg
            if(new_g < distance[nn]):#틀렸던 부분1(w가 아니라 distance 값과 비교해야 함)
                distance[nn] = new_g
                heapq.heappush(q, (new_g, nn))
    mx = 0
    cnt = 0
    for i in range(1,n+1):
        if(i != start and distance[i] != INF):
            mx = max(mx, distance[i])
            cnt+=1
    return (cnt, mx)



n,m,c = map(int, input().split())
graph = [[] for _ in range(n+1)]#틀렸던 부분 2(범위)
for _ in range(m):
    x,y,z = map(int, input().split())
    graph[x].append((y,z))#노드, 무게
distance = [INF] * (n+1)

cnt,tm = dijkstra(graph, c)
print(cnt, tm)

