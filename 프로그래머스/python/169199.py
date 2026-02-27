from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(graph, sx, sy, tx, ty, n, m):
    q = deque()
    visit = [[False] * m for _ in range(n)]
    visit[sx][sy] = True
    q.append((0,sx, sy))
    while q:
        cnt,x,y = q.popleft()
        if(x == tx and y == ty):
            return cnt
        
        for k in range(4):
            nx, ny = x,y
            while(0<=nx<n and 0<=ny<m and graph[nx][ny] != 'D'):
                nx+=dx[k]
                ny+=dy[k]
            nx-=dx[k]
            ny-=dy[k]
            if(visit[nx][ny] == False):
                visit[nx][ny] = True
                q.append((cnt+1, nx, ny))
    return -1
            
        


def solution(board):
    n = len(board)
    m = len(board[0])
    cnt = 0
    start_x, start_y = 0,0
    target_x, target_y = 0,0
    gOrStop = 0
    for i in range(n):
        for j in range(m):
            if(board[i][j] == 'R'):
                start_x, start_y = i,j
                cnt+=1
            if(board[i][j] == 'G'):
                target_x, target_y = i,j
                cnt+=1
            if(cnt == 2):
                gOrStop = 1
                break
        if(gOrStop == 1):
            break
    return bfs(board, start_x, start_y, target_x, target_y, n, m)
        
                