import sys
from itertools import combinations
input = sys.stdin.readline
import copy
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(graph, x, y):
    graph[x][y] = 3
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if(0<= nx< n and 0<= ny < m and graph[nx][ny] == 0):
            dfs(graph, nx, ny)
            
def safe(graph):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if(graph[i][j] == 0):
                cnt+=1
    return cnt


n,m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
lst = []
for i in range(n):
    for j in range(m):
        if(graph[i][j] == 0):
            lst.append((i,j))
lst = list(combinations(lst, 3))
max_cnt = 0
for l in lst:
    tmp = copy.deepcopy(graph)
    (x1,y1), (x2, y2), (x3, y3) = l
    tmp[x1][y1] = tmp[x2][y2] = tmp[x3][y3] = 1
    for i in range(n):
        for j in range(m):
            if(tmp[i][j] == 2):
                dfs(tmp, i, j)
    sf = safe(tmp)
    max_cnt = max(sf, max_cnt)

print(max_cnt)
        
