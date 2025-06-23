import sys
input = sys.stdin.readline

n,m,k = map(int, input().split())

lst = list(map(int, input().split()))
lst.sort()
first = lst[n-1]
second = lst[n-2]
count = int(m / (k+1)) * k
count += m % (k+1)
ans = count * first + (m - count) * second
print(ans)