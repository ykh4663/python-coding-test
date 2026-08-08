from collections import deque

def solution(n, friendships, m, k):
    answer = []
    graph = [[] for _ in range(n+1)]
    for x,y in friendships:
        graph[x].append(y)
        graph[y].append(x)
    
    visit = [False] * (n+1)

    q = deque()
    q.append(m)
    answer.append(m)
    visit[m] = True

    while q:
        nd = q.popleft()
        for node in graph[nd]:
            if(len(answer) == k):
                answer.sort()
                return answer
            if(visit[node] == False):
                answer.append(node)
                q.append(node)
                visit[node] = True

       


    return answer



N = 5
friendships = [[1,2],[2,3],[3,4],[4,5]]
M = 1
K = 3

print(solution(N, friendships, M, K))