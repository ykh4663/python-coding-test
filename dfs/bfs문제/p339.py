import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)
def bfs(graph, k, x):
    q = deque()
    visit[x] = True
    q.append((x, 0))
    rs = []
    while q:
        elem,cnt = q.popleft()
        if(cnt > k):
            break
        if(cnt == k):
            rs.append(elem)
        for g in graph[elem]:
            if(visit[g] ==False):
                q.append((g, cnt+1))
                visit[g] = True
    return rs
    
        
n,m,k,x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
visit = [False] * (n+1)
rs = bfs(graph, k, x)
rs.sort()
if(len(rs) == 0):
    print(-1)
else:
    for r in rs:
        print(r)



#주의할 점 : 무분별하게 heapq에 넣으면 메모리 초과 뜸-> 대안 : 항상 visit 여부 확인하기
