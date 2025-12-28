# import sys
# from itertools import combinations
# from collections import deque
# input = sys.stdin.readline

# dx = [1,-1,0,0]
# dy = [0,0,1,-1]

# def bfs(graph, x, y):
#     cnt = 0
#     for k in range(4):
#         q = deque()
#         q.append((x,y))
#         gOrStop = 0
#         while(q):
#             a,b = q.popleft()
#             nx = a + dx[k]
#             ny = b + dy[k]
#             if(0<= nx < n and 0<= ny < n):
#                 if(graph[nx][ny] == 'S'):
#                     return False
#                 if(graph[nx][ny] == 'O'):
#                     gOrStop = 0
#                     break
#                 q.append((nx, ny))
#             if(gOrStop == 1):
#                 break
        
#     return True          
                


# n = int(input())
# lst = []
# for _ in range(n):
#     lst.append(list(map(str, input().split())))
# teacher_lst = []
# array = []
# for i in range(n):
#     for j in range(n):
#         if(lst[i][j] == 'T'):
#             teacher_lst.append((i,j))
#         if(lst[i][j] == 'X'):
#             array.append((i,j))
# array = list(combinations(array, 3))
# gOrStop = False
# for ar in array:
#     (a,b), (c,d), (e,f) = ar
#     lst[a][b] = lst[c][d] = lst[e][f] = 'O'
#     for t in teacher_lst:
#         x,y = t
#         if(bfs(lst, x, y)==False):
#             gOrStop = True
#             break
#     if(gOrStop == False):
#         break   
#     lst[a][b] = lst[c][d] = lst[e][f] = 'X'
    
    
# if(gOrStop):
#     print("NO")
# else:
#     print("YES")


    

import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(grid, x, y):
    # (x,y) 위치의 선생님이 네 방향 중 한 곳이라도
    # 학생을 발견하면 False, 모두 못 보면 True
    for k in range(4):
        nx, ny = x, y
        while True:
            nx += dx[k]
            ny += dy[k]
            # 경계를 벗어나면 이 방향 탐색 종료
            if not (0 <= nx < n and 0 <= ny < n):
                break
            # 장애물 만나면 시야 차단
            if grid[nx][ny] == 'O':
                break
            # 학생을 만나면 탐지 실패
            if grid[nx][ny] == 'S':
                return False
    return True

n = int(input())
grid = [input().split() for _ in range(n)]

teachers = []
empties = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 'T':
            teachers.append((i, j))
        elif grid[i][j] == 'X':
            empties.append((i, j))

found_safe = False
for walls in combinations(empties, 3):
    # 1) 장애물 설치
    for wx, wy in walls:
        grid[wx][wy] = 'O'
    # 2) 모든 선생님이 한 명도 학생을 못 보는지 확인
    invalid = False
    for tx, ty in teachers:
        if not bfs(grid, tx, ty):
            invalid = True
            break
    if not invalid:
        found_safe = True
        break
    # 3) 실패 시 장애물 되돌리기
    for wx, wy in walls:
        grid[wx][wy] = 'X'

# 결과 출력
if found_safe:
    print("YES")
else:
    print("NO")



    
