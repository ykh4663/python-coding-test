import sys
input = sys.stdin.readline

n,k = map(int, input().split())
lst = [0] * (n+1)

for i in range(1,n):
    lst[i+1] = lst[i]+1
    if((i+1) % k == 0):
        lst[i+1] = min(lst[i+1], lst[(i+1)//k]+1)
print(lst[n])
