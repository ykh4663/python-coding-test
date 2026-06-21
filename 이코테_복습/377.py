import sys
n = int(input())

lst = []
for _ in range(n):
    t,p = map(int, input().split())
    lst.append((t,p))
dp = [0] * (n+2)
for i in range(n-1, -1, -1):
    dp[i] = dp[i+1]
    now_t, now_p = lst[i]
    if(now_t + i > n):
        continue
    dp[i] = max(dp[i], now_p + dp[i + now_t])
    
print(dp[0])
