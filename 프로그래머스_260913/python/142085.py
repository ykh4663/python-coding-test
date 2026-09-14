import heapq
def solution(n, k, enemy):
    answer = 0
    q = []
    elen = len(enemy)
    cnt = 0
    for i in range(elen):
        n -= enemy[i]
        cnt+=1
        heapq.heappush(q, -enemy[i])
        if(n < 0):
            if(k <= 0):
                cnt-=1
                break
            elem = -heapq.heappop(q)
            n += elem
            k-=1
    return cnt
            
                
            
            
        
    
    
    
    
    return answer
