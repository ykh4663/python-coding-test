# 2,2 2,3 2,4
# 3,2     3,4
# 4,2     4,4
# 5,2 5,3 5,4
import copy
def rotate(sx, sy, ex, ey, graph, tmp, rlen, clen):
    mn = int(1e9)
    x,y = sx, sy+1
    while(y<=ey):
        tmp[x][y] = graph[x][y-1]
        mn = min(mn, tmp[x][y])
        y+=1
    y-=1
    x+=1

    while(x<=ex):
        
        tmp[x][y] = graph[x-1][y]
        mn = min(mn, tmp[x][y])
        x+=1

    x-=1
    y-=1

    while(y >= sy):
        
        tmp[x][y] = graph[x][y+1]
        mn = min(mn, tmp[x][y])
        y-=1

    y+=1
    x-=1

    while(x >= sx):
        
        tmp[x][y] = graph[x+1][y]
        mn = min(mn, tmp[x][y])
        x-=1

    return (tmp, mn)

        
            
        

def solution(rows, columns, queries):
    graph = [[0] * columns for _ in range(rows)]
    idx = 1
    for i in range(rows):
        for j in range(columns):
            graph[i][j] = idx
            idx+=1
    ans = []
    for q in queries:
        sx, sy, ex, ey = q
        tmp = copy.deepcopy(graph) # deepcopy를 매번 안해버리고 갱신하는 방식으로 할 경우 이상한 값 바라볼 수 있음
        (graph, mn) = rotate(sx-1, sy-1, ex-1, ey-1, graph, tmp, rows, columns)
        ans.append(mn)
    return ans
            

rows = 6
cols = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
result = solution(rows, cols, queries)
print(result)