import sys
input = sys.stdin.readline

n,c = map(int, input().split())
array = []
for _ in range(n):
    array.append(int(input()))
array.sort()
left = 1
right = array[-1] - array[0]
ans = 0
while(left <= right):
    gap = (left + right) //2
    cnt = 1
    value = array[0]
    for i in range(1,n):
        if(array[i] - value >= gap):
            cnt+=1
            value = array[i]
    if(cnt < c):
        right = gap-1
    else:
        ans = gap
        left = gap + 1
print(ans)


