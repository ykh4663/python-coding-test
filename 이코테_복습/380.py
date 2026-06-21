# n = int(input())
# lst = list(map(int, input().split()))

# dp = [0] * (n)

# for i in range(n-1, -1, -1):
#     if(i == n-1):
#         dp[i] = 1
#     else:
#         if(lst[i] <= lst[i+1]):
#             idx = i+2
#             while(idx != n):
#                 if(lst[i] > lst[idx]):
#                     break
#                 idx+=1
#             if(idx == n):
#                 elem = 1
#             else:
#                 elem = dp[idx] + 1
#             if(dp[i+1] > elem):
#                 dp[i] = dp[i+1]
#             else:
#                 dp[i] = elem
#         else:
#             dp[i] = dp[i+1] + 1
# print(n - dp[0])

n = int(input())
array = list(map(int, input().split()))
# 순서를 뒤집어 '최장 증가 부분 수열' 문제로 변환 -> reverse하면 좀 더 직관적이라서 이렇게 한 것이지 꼭 이렇게 할 필요는 없음
array.reverse()

# 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화
dp = [1] * n

# 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 열외해야 하는 병사의 최소 수를 출력
print(n - max(dp))