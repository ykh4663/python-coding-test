from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(graph, start, end, n, m):
    visit = [[False] * m for _ in range(n)]
    sx, sy = start
    ex, ey = end
    q = deque()
    q.append((0,sx, sy))
    visit[sx][sy] = True
    while q:
        w, x, y = q.popleft()
        if(ex == x and ey == y):
            return w
        for k in range(4):
            nx, ny = x,y
            while(0<=nx<n and 0<=ny<m and graph[nx][ny] != 'D'):
                nx += dx[k]
                ny += dy[k]
            nx -= dx[k]
            ny -= dy[k]
            if(visit[nx][ny] == True):
                continue
            visit[nx][ny] = True
            q.append((w+1, nx, ny))
    return -1
            
        

def solution(board):
    answer = 0
    n = len(board)
    m = len(board[0])
    start, end = 0,0
    secnt = 0
    for i in range(n):
        gOrStop = 0
        for j in range(m):
            if(board[i][j] == 'R'):
                start = (i,j)
                secnt+=1
            elif(board[i][j] == 'G'):
                end = (i,j)
                secnt+=1
            if(secnt == 2):
                gOrStop = 1
                break
        if(gOrStop == 1):
            break
    answer = bfs(board, start, end, n, m)
    
    return answer
board = [".D.R", "....", ".G..", "...D"]
result = solution(board)
print(result)