import sys
input = sys.stdin.readline

ball = [0] * 11
n,m = map(int, input().split())
w = list(map(int,input().split()))
for idx in w:
    ball[idx] +=1

total = 0
for i in range(m):
    n -= ball[i]
    total += (n * ball[i])
print(total)
