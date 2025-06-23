import sys
input = sys.stdin.readline

n,m = map(int, input().split())
max_value = -1
for _ in range(n):
    lst = list(map(int,input().split()))
    min_value = min(lst)
    max_value = max(max_value, min_value)
print(max_value)
