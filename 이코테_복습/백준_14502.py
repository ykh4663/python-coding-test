from itertools import combinations
import copy
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(graph, visit, i,j,n,m):
    q = deque()
    q.append((i,j))
    visit[i][j] = True
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if(0<=nx<n and 0<=ny<m):
                if(visit[nx][ny] == False and graph[nx][ny] == 0):
                    graph[nx][ny] = 2
                    visit[nx][ny] = True
                    q.append((nx, ny))
    


def check_safe(lst,n,m):
    result=  0
    graph = copy.deepcopy(lst)
    visit = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if(graph[i][j] == 2 and visit[i][j] == False):
                bfs(graph, visit, i,j, n,m)
    for i in range(n):
        for j in range(m):
            if(graph[i][j] == 0):
                result +=1
    return result


n,m = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

idx_lst = [(i,j) for i in range(n) for j in range(m)]
comb = list(combinations(idx_lst, 3))
mx_safe = 0
for c in comb:
    (c1_x, c1_y), (c2_x, c2_y), (c3_x, c3_y) = c
    if(lst[c1_x][c1_y] > 0 or lst[c2_x][c2_y] > 0 or lst[c3_x][c3_y] > 0):
        continue
    lst[c1_x][c1_y] = lst[c2_x][c2_y] = lst[c3_x][c3_y] = 1
    safe = check_safe(lst,n,m)
    mx_safe = max(mx_safe, safe)
    lst[c1_x][c1_y] = lst[c2_x][c2_y] = lst[c3_x][c3_y] = 0
print(mx_safe)


