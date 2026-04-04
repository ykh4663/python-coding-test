#X : 바다, 숫자 : 무인도
#상하좌우 연결 땅은 무인도
#숫자는 식량 - 상하좌우 연결되어있는 숫자 합은 무인도 몇일 머무르는지를 나타냄
from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(graph, visit, s_x, s_y, r, c):
    q = deque()
    q.append((s_x, s_y))
    visit[s_x][s_y] = True
    s = 0
    while q:
        x,y = q.popleft()
        s += int(graph[x][y])
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if(0<=nx<r and 0<=ny<c):
                if(visit[nx][ny] == False and graph[nx][ny] != 'X'):
                    q.append((nx, ny))
                    visit[nx][ny] = True
    return s

        


def solution(maps):
    r = len(maps)
    c = len(maps[0])
    
    ans = []
    visit = [[False] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if(maps[i][j] != 'X' and visit[i][j] == False):
                ans.append(bfs(maps, visit, i, j, r, c))
    
    if(len(ans) == 0):
        ans.append(-1)
    ans.sort()
    return ans
            
    
    
maps = ["XXX","XXX","XXX"]
print(solution(maps))