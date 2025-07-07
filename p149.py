import sys
input = sys.stdin.readline
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(graph, i, j):
    graph[i][j] = 1
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if(0<= nx < n and 0<= ny < m and graph[nx][ny] ==0):
            dfs(graph, nx, ny)
    

            

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))
cnt= 0
for i in range(n):
    for j in range(m):
        if(graph[i][j] == 0):
            dfs(graph, i, j)
            cnt+=1
print(cnt)


