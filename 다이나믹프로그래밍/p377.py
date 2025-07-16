import sys
input = sys.stdin.readline
n = int(input())
t = [0] * (n+1)
p = [0] * (n+1)
dp = [0] * (n+2)
for i in range(1,n+1):
    t[i], p[i] = map(int, input().split())

for i in range(n, 0, -1):
    dp[i] = dp[i+1]
    if(i + t[i] <= n+1):
        dp[i] = max(dp[i], p[i] + dp[i + t[i]])
print(dp[1])
