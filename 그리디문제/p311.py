import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

array.sort()
fear = 0
cnt = 0
for i in range(n):
    fear += 1
    if(array[i]<= fear):
        cnt+=1
        fear = 0
print(cnt)

