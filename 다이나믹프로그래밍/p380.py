# import sys
# input = sys.stdin.readline

# n = int(input())
# lst = list(map(int,input().split()))
# dp = [0] * n
# cnt = [0] * n
# for i in range(n-1, -1, -1):
#     dp[i] = lst[i]
#     cnt[i] = 1
#     for j in range(i+1, n):
#         if(lst[i] >= lst[j] and dp[i] < lst[i] + dp[j]):
#             dp[i] = lst[i] + dp[j]
#             cnt[i] = cnt[j] + 1
# mx_idx = -1
# mx = -1
# print(cnt)
# for i in range(n):
#     if(mx < dp[i]):
#         mx = dp[i]
#         mx_idx = i
# print(n - cnt[mx_idx])

#위 코드는 전투력 최대 합 하면서 내림차순할 때 열외시킬 병사 수 구한 것



import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

dp = [1] * n
for i in range(1,n):
    for j in range(i):
        if(lst[i] < lst[j] and dp[i] < dp[j] + 1):
            dp[i] = dp[j] + 1
            
print(n - max(dp))