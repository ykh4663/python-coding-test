import sys
input = sys.stdin.readline

#key 부분이 1이고 lock 부분이 0이어야 한다
#lock 부분이 1이고 key 부분이 1일 수는 없다
#key부분 1이고 lock 부분 0인 것의 개수가 lock에서 0의 개수 만큼 있어야한다(cnt가)
#lock을 가로 세로 늘려서 생각하기

def rotate(key):
    m = len(key)
    new_key = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            new_key[j][m-1-i] = key[i][j]
    return new_key

def okay(key, graph ,i, j):
    m = len(key)
    filled = 0
    for x in range(m):
        for y in range(m):
            if(key[x][y] == 1):
                if(graph[x + i][y + j] == 1):
                    return -1
                elif(graph[x+i][y+j] == 0):
                    filled+=1
    return filled

def solution(key, lock):
    
    n,m = len(lock), len(key)
    cnt = 0
    for i in range(n):
        cnt += lock[i].count(0)
    
    graph = [[-1] * (3*n) for _ in range(3*n)]
    
    for i in range(n):
        for j in range(n):
            graph[i+n][j+n] = lock[i][j]
    
    for _ in range(4):
        for i in range(1,2*n+1):
            for j in range(1, 2*n+1):
                local_cnt = okay(key, graph ,i, j)
                if(local_cnt == cnt):
                    return True
            

                
        key = rotate(key)
 

    return False

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
result = solution(key, lock)
print(result)