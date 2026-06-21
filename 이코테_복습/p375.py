import copy
dx = [-1,0,1]
dy = [-1,-1,-1]

T = int(input())


for _ in range(T):
    n,m = map(int, input().split())
    graph = []
    tmp = list(map(int, input().split()))
    for i in range(0,len(tmp),m):
        elem = tmp[i:i+m]
        graph.append(elem)
    dp = copy.deepcopy(graph)
    for y in range(1,m):
        for x in range(n):
            for k in range(3):
                nx = x + dx[k]
                ny = y + dy[k]
                if(0<=nx<n and 0<=ny<m):
                    dp[x][y] = max(dp[x][y], graph[x][y] + dp[nx][ny])
    
    ans = -1
    for i in range(n):
        ans = max(ans, dp[i][m-1])
    print(ans)





    
        
