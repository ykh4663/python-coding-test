import sys
input = sys.stdin.readline
INF = int(1e9)
n,m = map(int, input().split())
dollar = []
dp = [INF] * 10001
dp[0] = 0
for _ in range(n):
    dollar.append(int(input()))
for d in dollar:
    idx = d
    while(idx <= m):
        dp[idx] = min(dp[idx-d] + 1, dp[idx])
        idx+=d
if(dp[m] == INF):
    print(-1)
else:
    print(dp[m])