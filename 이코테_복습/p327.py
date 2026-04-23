from collections import deque
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def move_snake(q, graph, k, n):
    x,y = q[-1]
    nx = x + dx[k]
    ny = y + dy[k]
    if(0<=nx<n and 0<=ny<n and graph[nx][ny] != 2):
        q.append((nx, ny))
        if(graph[nx][ny] == 1):
            graph[nx][ny] = 2
        else:
            graph[nx][ny] = 2
            qx, qy = q.popleft()
            graph[qx][qy] = 0  
        return True
    else:
        return False

    




n = int(input())

graph = [[0] * n for _ in range(n)]
q = deque()
q.append((0,0))
graph[0][0] = 2
k = 0


a = int(input())
for _ in range(a):
    x,y = map(int, input().split())
    graph[x-1][y-1] = 1

t = int(input())
time_lst = [0] * 10001
dir_lst = ['O'] * 10001 
for _ in range(t):
    time, dl = map(str, input().split())
    time = int(time)
    time_lst[time] = 1
    dir_lst[time] = dl
idx = 1
while True:
    
    if(move_snake(q, graph, k, n)== False):
        break
    if(time_lst[idx] == 1):
        if(dir_lst[idx] == 'D'):
            k = (k+1) % 4
        else:
            k = (k-1) % 4
    idx+=1
print(idx)

    

