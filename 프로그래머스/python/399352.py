from itertools import combinations


def solution(n, q, ans):
    
    comb = [i for i in range(1,n+1)]
    comb = list(combinations(comb, 5))
    
    answer = 0
    
    for c in comb:
        q_len = len(q)
        tot_cnt = 0
        for i in range(q_len):
            dp = [0] * (n+1)
            lst = q[i]
            for l in lst:
                dp[l]+=1
            cnt = 0
            for cc in c:
                if(dp[cc] == 0):
                    continue
                else:
                    cnt+=1
            if(cnt == ans[i]):
                tot_cnt+=1
        if(tot_cnt == q_len):
            answer+=1

    return answer


n = 15
q = [[2, 3, 9, 12, 13], [1, 4, 6, 7, 9], [1, 2, 8, 10, 12], [6, 7, 11, 13, 15], [1, 4, 10, 11, 14]]
ans = [2, 1, 3, 0, 1]
result = solution(n,q,ans)
print(result)