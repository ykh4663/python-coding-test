import sys
from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(graph, visit, sx, sy, group):
    global n, l, r
    q= deque()
    q.append((sx, sy))
    tmp = []
    tmp.append((sx, sy))
    visit[sx][sy] = True
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if(0<=nx<n and 0<=ny<n):
                if(visit[nx][ny] == False):
                    elem = abs(graph[x][y] - graph[nx][ny])
                    if(l<=elem<=r):
                        tmp.append((nx, ny))
                        visit[nx][ny] = True
                        q.append((nx, ny))
    if(len(tmp) == 1):
        return False
    else:
        group.append(tmp)
        return True



n,l,r = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

idx = 0
while True:
    visit = [[False] * n for _ in range(n)]
    group = []
    cnt = 0
    for i in range(n):
        for j in range(n):
            if(visit[i][j] == False):
                if(bfs(graph, visit, i, j, group) == True):
                    cnt+=1
    if(cnt == 0):
        break
    else:
        idx+=1
    for glst in group:
        g_sum = 0
        for g in glst:
            gx, gy = g
            g_sum+=graph[gx][gy]
        elem = g_sum // len(glst)
        for gg in glst:
            ggx, ggy = gg
            graph[ggx][ggy] = elem

print(idx)




