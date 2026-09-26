def find_cycle(cards, elem, visit):
    cnt = 0
    while True:
        if(visit[elem] == True):
            break
        visit[elem] = True

        elem = cards[elem]-1
        cnt+=1
    return cnt

def solution(cards):
    n = len(cards)
    lst = [0] * (n+1)
    visit = [False] * n
    cnt = 0
    for i in range(n):
        if(visit[i] == True):
            continue
        idx = find_cycle(cards, i, visit)

        lst[idx] +=1
        cnt+=1
        
        
    if(cnt <= 1):
        return 0
    else:
        first = 0
        for i in range(n,0,-1):
            if(lst[i] > 0):
                if(lst[i] > 1):
                    if(first == 0):
                        return i * i
                    else:
                        return first * i
                elif(lst[i] == 1):
                    if(first == 0):
                        first = i
                    else:
                        return first * i
        
        
                        
                
                
                    
            
            
        
cards = [8,6,3,7,2,5,1,4]	
result = solution(cards)
print(result)
