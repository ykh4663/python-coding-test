from itertools import combinations

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
hous = []
chicken = []
for i in range(n):
    for j in range(n):
        if(graph[i][j] == 1):
            hous.append((i,j))
        elif(graph[i][j] == 2):
            chicken.append((i,j))
comb = list(combinations(chicken, m))
ans = int(1e9)
for c in comb:
    mn = 0
    for h in hous:
        local_mn = int(1e9)
        hx, hy  = h
        for i in range(m):
            x,y = c[i]
            local_mn = min((abs(hx-x) + abs(hy - y)), local_mn)
        mn+=local_mn
    ans = min(mn, ans)
print(ans)
    
        
            
        



