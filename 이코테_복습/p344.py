from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]
n,k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
s,x,y = map(int, input().split())
q = deque()
for elem in range(1,k+1):
    for i in range(n):
        for j in range(n):
            if(graph[i][j] == elem):
                q.append((0,i,j))
while q:
    cnt, a, b = q.popleft()
    if(cnt == s):
        break
    for kk in range(4):
        nx = a + dx[kk]
        ny = b + dy[kk]
        if(0<=nx<n and 0<=ny<n):
            if(graph[nx][ny] != 0):
                continue
            else:
                graph[nx][ny] = graph[a][b]
                q.append((cnt+1, nx, ny))
print(graph[x-1][y-1])


        

