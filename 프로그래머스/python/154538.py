# g_cnt = -1
# visit = [False] * (int(1e6)+1)

# def dfs(cnt, x,y,n):
#     global g_cnt, visit
#     if(x == y):
#         g_cnt = cnt
#         return
#     if(y - n > 0 and visit[y - n] == False):
#         visit[y-n] = True
#         dfs(cnt+1, x,y-n, n)
#     if(y % 2 == 0 and y // 2 > 0 and visit[y//2] == False):
#         visit[y//2] = True
#         dfs(cnt+1,x, y//2, n)
#     if(y % 3 == 0 and y // 3 > 0 and visit[y//3] == False):
#         visit[y//3] == True
#         dfs(cnt+1,x, y//3, n)
# def solution(x, y, n):
#     global g_cnt
#     dfs(0, x, y, n)
#     return g_cnt

# x = 10
# y = 40
# n = 5
# print(solution(x,y,n))
INF = int(1e6)
from collections import deque

def solution(x, y, n):
    if x == y:
        return 0
    # 큐에는 (현재 숫자, 연산 횟수)를 담습니다.
    q = deque()
    q.append((y,0))
    visited = [False] * (INF+1)
    
    while q:
        curr, cnt = q.popleft()
        # 1. n을 빼는 경우
        if curr - n == x: 
            return cnt + 1
        if curr - n > x and visited[curr - n] == False:
            visited[curr-n] = True
            q.append((curr - n, cnt + 1))
            
        # 2. 2로 나누는 경우
        if curr % 2 == 0:
            if curr // 2 == x: 
                return cnt + 1
            if curr // 2 > x and visited[curr // 2] == False:
                visited[curr // 2] == True
                q.append((curr // 2, cnt + 1))
                
        # 3. 3으로 나누는 경우
        if curr % 3 == 0:
            if curr // 3 == x: 
                return cnt + 1
            if curr // 3 > x and visited[curr // 3] == False:
                visited[curr // 3] == True
                q.append((curr // 3, cnt + 1))
                
    return -1

x = 10
y = 40
n = 5
print(solution(x,y,n))