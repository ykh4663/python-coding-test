#visit 도입 대신 3으로 바꿔가면서 풀기
from itertools import combinations
from collections import deque
import copy

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(graph, sx, sy, n, m):
    q = deque()
    q.append((sx, sy))
    graph[sx][sy] = 3
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if(0<=nx<n and  0<=ny<m):
                if(graph[nx][ny]== 0 or graph[nx][ny] == 2):
                    graph[nx][ny] = 3
                    q.append((nx, ny))

def findSafe(graph, n, m):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if(graph[i][j] == 0):
                cnt+=1
    return cnt
    


n,m = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

comb = []
for i in range(n):
    for j in range(m):
        if(lst[i][j] == 0):
            comb.append((i,j))
comb = list(combinations(comb, 3))
total = 0
for c in comb:
    graph = copy.deepcopy(lst)
    (x1, y1), (x2, y2), (x3, y3) = c
    graph[x1][y1] = graph[x2][y2] = graph[x3][y3] = 1
    for i in range(n):
        for j in range(m):
            if(graph[i][j] == 2):
                bfs(graph, i, j, n, m)
    
    total = max(total, findSafe(graph, n, m))
print(total)
