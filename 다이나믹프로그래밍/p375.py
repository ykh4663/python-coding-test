# import sys
# input = sys.stdin.readline
# dx = [-1,0,1]
# dy = [-1,-1,-1]

# t = int(input())
# for _ in range(t):
    
#     n,m =map(int,input().split())
#     gold = []
#     lst = list(map(int, input().split()))
#     for i in range(0,len(lst), m):
#         gold.append(lst[i:i+m])
#     dp = [[0] * m for _ in range(n)]
#     for i in range(n):
#         dp[i][0] = gold[i][0]
#     for j in range(1,m):
#         for i in range(n):
#             for k in range(3):
#                 nx = i + dx[k]
#                 ny = j + dy[k]
#                 if(0<=nx < n and 0<= ny < m):
#                     dp[i][j] = max(dp[i][j], dp[nx][ny] + gold[i][j])
#     mx = -1
#     for i in range(n):
#         mx = max(mx, dp[i][m-1])
#     print(mx)
        

import sys
input = sys.stdin.readline
dx = [-1,0,1]
dy = [-1,-1,-1]

t = int(input())
for _ in range(t):
    
    n,m =map(int,input().split())
    gold = []
    lst = list(map(int, input().split()))
    for i in range(0,len(lst), m):
        gold.append(lst[i:i+m])
    for j in range(1,m):
        for i in range(n):
            best = 0
            for k in range(3):
                nx = i + dx[k]
                ny = j + dy[k]
                if(0<=nx < n and 0<= ny < m):
                    best = max(best, gold[nx][ny])
            gold[i][j] += best
    mx = -1
    for i in range(n):
        mx = max(mx, gold[i][m-1])
    print(mx)
        
    

    
    

    
#주석 단 부분은 dp 배열 하나 더 추가해서 푼 case이고 아래 경우는 gold 배열 하나에서 로직 다 처리함