# #40점짜리 풀이-> 틀린 이유 : 컴비네이션으로 돌아가면서 시간복잡도 문제 터짐
# from itertools import combinations
# INF = int(1e9)

# def solution(info, n, m):
#     info_len = len(info)
#     dp = []#0이면 A, 1이면 B
#     comb = [i for i in range(info_len)]
#     min_a_cnt = INF
#     for i in range(info_len+1):
#         local_comb = list(combinations(comb, i))
        
#         for lc in local_comb:
            
#             dp = [0] * info_len
#             a_cnt, b_cnt = 0,0
#             for llc in lc:
#                 dp[llc]+=1
#             for j in range(info_len):
#                 if(dp[j] == 0):
#                     a_cnt+=info[j][0]
#                 else:
#                     b_cnt+=info[j][1]
#             if(a_cnt < n and b_cnt < m):
#                 min_a_cnt = min(min_a_cnt, a_cnt)
        
#     if(min_a_cnt == INF):
#         return -1
#     return min_a_cnt

            





# info = [[1, 2], [2, 3], [2, 1]]
# n = 1
# m = 7
# result = solution(info, n, m)
# print(result)#2


INF = int(1e9)

def solution(info, n, m):
    dp = [INF] * n #n을 넘으면 안되기 때문에
    dp[0] = 0#처음 a값이 0일 때 b값 중 될 수 있는 최소값은 아무것도 선택 안하는 것
    
    for a_info, b_info in info:
        new_dp = [INF] * n

        for a in range(n):
            if(dp[a] == INF):#b값이 결정 안되면 스킵
                continue

            #b가 이번에 가질 때
            nb = dp[a] + b_info
            if(nb < m):#b가능한 값이 m미만이므로
                if(nb < new_dp[a]):#b 선택지 작을 수록 유리하므로(향후 b에 더 많이 뽑아서 a값이 줄어드므로)
                    new_dp[a] = nb
            
            na = a + a_info#a가 택한 경우
            if(na < n):#n미만의 값 중에서
                if(dp[a] < new_dp[na]):#최신화하려는 a값의 b가 더 작은 거를 택일
                    new_dp[na] = dp[a]
        dp = new_dp#최신화된 값 매번 갱신해주기
    ans = INF
    for a in range(n):#b값이 m을 넘지 않은 것 중에 a 최솟값 찾기
        if(new_dp[a] < m):
            ans = min(ans, a)
    if(ans == INF):
        return -1
    return ans    
    
    
            
        

                




# 테스트
info = [[1, 2], [2, 3], [2, 1]]
n = 4
m = 4
print(solution(info, n, m))  