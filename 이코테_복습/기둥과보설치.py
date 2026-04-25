def isKi(x, y, n, graph):
    # 1. 바닥 위인가?
    if y == 0:
        return True
    # 2. 다른 기둥 위인가? (내 위치 바로 아래에 기둥이 있는지)
    if y - 1 >= 0 and 0 in graph[x][y-1]:
        return True
    # 3. 보의 한쪽 끝부분 위인가? (내 위치에서 보가 시작하거나, 왼쪽에서 보가 오거나)
    if 1 in graph[x][y]:
        return True
    if x - 1 >= 0 and 1 in graph[x-1][y]:
        return True
        
    return False

def isBo(x, y, n, graph):
    # 1. 한쪽 끝부분이 기둥 위인가? (왼쪽 아래에 기둥이 있거나, 오른쪽 아래에 기둥이 있거나)
    if y - 1 >= 0 and 0 in graph[x][y-1]:
        return True
    if x + 1 <= n and y - 1 >= 0 and 0 in graph[x+1][y-1]:
        return True
    # 2. 양쪽 끝부분이 다른 보와 동시에 연결되어 있는가?
    if x - 1 >= 0 and x + 1 <= n and 1 in graph[x-1][y] and 1 in graph[x+1][y]:
        return True
        
    return False

def solution(n, build_frame):
    answer = []
    # 한 칸에 기둥(0)과 보(1)가 같이 있을 수 있으므로 리스트[]로 초기화!
    graph = [[[] for _ in range(n + 1)] for _ in range(n + 1)]
    
    for x, y, a, b in build_frame:
        
        if b == 0: #삭제할 때
            # 1. 일단 지워본다 (Deepcopy 대신 직접 빼기)
            graph[x][y].remove(a)
            answer.remove([x, y, a])
            
            # 2. 남은 모든 구조물이 안전한지 확인한다
            is_safe = True
            for cx, cy, ca in answer:
                if ca == 0 and not isKi(cx, cy, n, graph):
                    is_safe = False
                    break
                elif ca == 1 and not isBo(cx, cy, n, graph):
                    is_safe = False
                    break
                    
            # 3. 안전하지 않으면 롤백 (다시 돌려놓기)
            if not is_safe:
                graph[x][y].append(a)
                answer.append([x, y, a])
                
        else: # 설치할 때
            # 1. 일단 설치해본다
            graph[x][y].append(a)
            
            # 2. 방금 설치한 얘 하나만 튼튼한지 확인한다
            is_safe = False
            if a == 0:
                is_safe = isKi(x, y, n, graph)
            else:
                is_safe = isBo(x, y, n, graph)
                
            # 3. 튼튼하면 answer에 넣고, 부실 공사면 롤백(제거)한다
            if is_safe:
                answer.append([x, y, a])
            else:
                graph[x][y].remove(a)

    # 문제의 요구사항에 맞게 정렬
    answer.sort()
    return answer

# 테스트
n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(n, build_frame))

