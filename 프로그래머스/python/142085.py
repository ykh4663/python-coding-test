import heapq

def solution(n, k, enemy):
    heap = []
    
    for i in range(len(enemy)):
        # 인덱스를 이용해 이번 라운드의 적의 수(요소 값)를 꺼냄.
        e = enemy[i] 
        
        # 1. 일단 무대포로 싸우고 병사(n)를 깎.
        n -= e
        
        # 2. 이번 라운드에 싸운 적의 수를 힙에 기록.
        heapq.heappush(heap, -e)
        
        
        if n < 0:
            
            if k > 0:
                max_enemy = -heapq.heappop(heap)
                n += max_enemy
                k -= 1
            
            else:
                return i # 현재 라운드(i)까지만 깰 수 있음
                
    
    return len(enemy)