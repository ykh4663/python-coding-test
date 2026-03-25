from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(maps, s,t):
    s_x, s_y = s
    t_x, t_y= t
    r,c = len(maps), len(maps[0])
    visit = [[False] * c for _ in range(r)]
    q = deque()
    q.append((0,s_x, s_y))
    while q:
        cnt, x, y = q.popleft()
        if(x == t_x and y == t_y):
            return cnt
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if(0<=nx<r and 0<=ny<c):
                if(maps[nx][ny] != 'X' and visit[nx][ny] == False):
                    visit[nx][ny] = True
                    q.append((cnt+1, nx, ny))
        

    return -1


def solution(maps):
    s,e,l = 0,0,0
    r,c = len(maps), len(maps[0])
    cnt = 0
    for i in range(r):
        for j in range(c):
            if(maps[i][j] == 'S'):
                s = (i,j)
                cnt+=1
            if(maps[i][j] == 'E'):
                e = (i,j)
                cnt+=1
            if(maps[i][j] == 'L'):
                l = (i,j)
                cnt+=1
            if(cnt == 3):
                break
        if(cnt == 3):
            break
    ans1 = bfs(maps, s,l)
    ans2 = bfs(maps, l,e)
    if(ans1 != -1 and ans2 != -1):
        return ans1+ans2
    else:
        return -1

            



maps = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]
result = solution(maps)
print(result)