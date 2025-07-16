import sys
input = sys.stdin.readline

# A를 B로 바꾸는 최소 편집 거리 계산
str1 = input().rstrip()   # 원본 문자열 A
str2 = input().rstrip()   # 목표 문자열 B

n = len(str1)
m = len(str2)

# dp[i][j]: A의 앞 i글자 → B의 앞 j글자로 바꾸는 최소 연산 횟수
dp = [[0] * (m+1) for _ in range(n+1)]

# 1) A의 i글자를 빈 문자열로 바꾸는 비용 (삭제만 i번)
for i in range(1, n+1):
    dp[i][0] = i

# 2) 빈 문자열을 B의 j글자로 만드는 비용 (삽입만 j번)
for j in range(1, m+1):
    dp[0][j] = j

# 3) 나머지 dp 테이블 채우기
for i in range(1, n+1):
    for j in range(1, m+1):
        if str1[i-1] == str2[j-1]:
            # 마지막 글자가 같으면, 그대로 대각선 값 가져옴
            dp[i][j] = dp[i-1][j-1]
        else:
            # 삽입, 삭제, 교체 중 최소값 + 1
            dp[i][j] = min(
                dp[i][j-1]   + 1,  # 삽입: B[j-1]을 A 끝에 삽입
                dp[i-1][j]   + 1,  # 삭제: A[i-1]을 삭제
                dp[i-1][j-1] + 1   # 교체: A[i-1] → B[j-1]
            )

# 4) 전체 A→B로 바꾸는 최소 연산 횟수 출력
print(dp[n][m])
#나중에 다시