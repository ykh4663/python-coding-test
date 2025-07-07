import sys
from collections import deque
input = sys.stdin.readline
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(graph):
    graph[0][0] = 0
    q = deque()
    q.append((0,0,1))
    while(q):
        x,y,c = q.popleft()
        if(x == n-1 and y == m-1):
            return c
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if(0<= nx < n and 0<= ny < m and graph[nx][ny] == 1):
                q.append((nx, ny, c+1))
                graph[nx][ny] = 0



n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))
cnt = bfs(graph)
print(cnt)
