from itertools import combinations
import sys

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def valid(graph, teachers, n):
    
    for t in teachers:
        x, y = t
        for k in range(4):
            nx, ny = x, y
            while True:
                nx += dx[k]
                ny += + dy[k]
                if(0<=nx<n and 0<=ny<n and graph[nx][ny] != 'O'):
                    if(graph[nx][ny] == 'S'):
                        return False
                else:
                    break
    return True

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(str, input().split())))
combs = []
teachers = []
for i in range(n):
    for j in range(n):
        if(graph[i][j] == 'X'):
            combs.append((i,j))
        elif(graph[i][j] == 'T'):
            teachers.append((i,j))
comb = list(combinations(combs, 3))
gOrStop = 0
for c in comb:
    c1, c2, c3 = c
    x1, y1 = c1
    x2, y2 = c2
    x3, y3 = c3
    graph[x1][y1] = graph[x2][y2] = graph[x3][y3] = 'O'
    if(valid(graph, teachers, n) == True):#모든 학생이 선생님 감시 피하면은
        gOrStop = 1
        break
    graph[x1][y1] = graph[x2][y2] = graph[x3][y3] = 'X'
if(gOrStop == 1):
    print('YES')
else:
    print("NO")
    
        

