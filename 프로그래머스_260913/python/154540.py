#무인도여행
from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(graph, visit, sx, sy, n, m):
    q = deque()
    q.append((sx, sy))
    visit[sx][sy] = True
    s = 0
    while q:
        x, y = q.popleft()
        s+= int(graph[x][y])
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if(0<=nx<n and 0<=ny<m):
                if(visit[nx][ny] == False and graph[nx][ny] != 'X'):
                    visit[nx][ny] = True
                    q.append((nx, ny))
    return s
            
        

def solution(maps):
    answer = []
    n = len(maps)
    m = len(maps[0])
    visit = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if(maps[i][j] != 'X' and visit[i][j] == False):
                answer.append(bfs(maps, visit, i, j, n, m))
    
    if(len(answer) == 0):
        return [-1]
    else:
        answer.sort()
        return answer

        

maps = ["X591X","X1X5X","X231X", "1XXX1"]
print(solution(maps))