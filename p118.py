import sys
input = sys.stdin.readline
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def makedir(direction):
    return direction % 4

def dfs(graph, x, y, direction):
    global cnt
    # (1) 현재 칸 청소
    graph[x][y] = 1
    cnt += 1

    # (2) 네 방향 탐색
    for _ in range(4):
        direction = makedir(direction - 1)  # 왼쪽 회전
        nx = x + dx[direction]
        ny = y + dy[direction]
        # (3) 범위 & 청소 전 칸인지 확인
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            dfs(graph, nx, ny, direction)
            return   # 일단 한 칸 이동하면 다시 4방향부터 재탐색

    # (4) 네 방향 다 안 됐으면 후진
    bx = x - dx[direction]
    by = y - dy[direction]
    if 0 <= bx < n and 0 <= by < m and graph[bx][by] != 1:
        dfs(graph, bx, by, direction)
    # else: 뒤도 벽이면 그냥 종료

# 입력 처리
n, m = map(int, input().split())
a, b, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
dfs(graph, a, b, d)
print(cnt)