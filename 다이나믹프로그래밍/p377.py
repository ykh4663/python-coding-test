import sys
input = sys.stdin.readline
n = int(input())
lst = []
for _ in range(n):
    lst.append((map(int, input().split())))
dp = [0] * (n+1)
#다시 풀기