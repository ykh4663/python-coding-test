import sys
input = sys.stdin.readline

dx = [-1,-1]
dy=  [-1, 0]

n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))
for i in range(1,n):
    for j in range(len(lst[i])):
        best = -1
        for k in range(2):
            nx = i + dx[k]
            ny = j + dy[k]
            if(0<= nx < n and 0<= ny < i):
                best = max(best,lst[nx][ny])
        lst[i][j] += best
print(max(lst[n-1]))
            
