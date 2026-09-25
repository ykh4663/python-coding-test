#미로 탈출
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(graph, sidx, eidx, n, m):
    q = deque()
    visit = [[False] * m for _ in range(n)]
    sx, sy = sidx
    ex, ey = eidx
    visit[sx][sy] = True
    q.append((0, sx, sy))
    while q:
        w, x, y = q.popleft()
        if(x == ex and y == ey):
            return w
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if(0<=nx<n and 0<=ny<m):
                if(graph[nx][ny] != 'X' and visit[nx][ny] == False):
                    visit[nx][ny] = True
                    q.append((w+1, nx, ny))
    return -1
        

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    start_idx, end_idx, labber_idx = 0,0,0
    for i in range(n):
        for j in range(m):
            if(maps[i][j] == 'S'):
                start_idx = (i,j)
            elif(maps[i][j] == 'E'):
                end_idx = (i,j)
            elif(maps[i][j] == 'L'):
                labber_idx = (i,j)
    labber_weight = bfs(maps, start_idx, labber_idx, n, m)
    if(labber_weight == -1):
        return -1
    end_weight = bfs(maps, labber_idx, end_idx, n, m)
    if(end_weight == -1):
        return -1
    return labber_weight + end_weight
    