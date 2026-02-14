# n = int(input())
# soldier = list(map(int, input().split()))

# dp = [0] * n
# cnt = [0] * n

# for i in range(n-1, -1, -1):
#     elem = soldier[i]
#     mx = soldier[i]
#     gOrStop = 0
#     idx = 0
#     for j in range(i,n):
#         if(elem > soldier[j]):
#             mx= max(mx, elem+dp[j])
#             idx = j
#             gOrStop = 1
#     if(gOrStop == 1):
#         dp[i] = mx
#         cnt[i] = dp[j]+1
#     else:
#         dp[i] = mx
#         cnt[i] = 1
# print(n-max(cnt))

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n
for i in range(n-1,-1,-1):
    gOrStop = 0
    for j in range(i+1, n):
        if(arr[i] > arr[j]):
            dp[i] = max(dp[i], dp[j]+1)
            gOrStop = 1
    if(gOrStop == 0):
        dp[i] = 1
print(n-max(dp))
