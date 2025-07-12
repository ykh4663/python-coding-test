import sys
from collections import deque
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n,k = map(int, input().split())
graph = [[0] * n for _ in range(n)]
q = deque()
for i in range(n):
    lst = list(map(int, input().split()))
    j = 0
    for l in lst:
        graph[i][j] = l
        if(l != 0):
            q.append((l, i, j, 0))
        j+=1
        

s,xx,yy = map(int,input().split())
q = deque(sorted(q))

while q:
    
    elem, x, y,cnt = q.popleft()
    if(cnt == s):
        break
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if(0<= nx < n and 0<= ny < n and graph[nx][ny] == 0):
            graph[nx][ny] = elem
            q.append((elem, nx, ny,cnt+1))
print(graph[xx-1][yy-1])
            
    

#deque에서 정렬하고 싶을 때는 q = deque(sorted(q)) 사용하기
#이거 하기 싫다면 그냥 초반꺼는 heapq에 저장해놓으면서 우선순위 큐 돌리기