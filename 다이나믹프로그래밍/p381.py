import sys
input = sys.stdin.readline


n = int(input())

dp = [0] * n
dp[0] = 1
i0 , i1, i2 = 0,0,0
n0, n1, n2 = 2,3,5
for i in range(1,n):
    next = min(n0, n1, n2)
    dp[i] = next
    if(next == n0):
        i0 +=1
        n0 = dp[i0] * 2
    if(next == n1):
        i1 +=1
        n1 = dp[i1] * 3
    if(next == n2):
        i2 +=1
        n2 = dp[i2] * 5
print(dp[n-1])
            

        
