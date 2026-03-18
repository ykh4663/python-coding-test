#할인행사 문제풀이
from collections import defaultdict

def solution(want, number, discount):
    d_len = len(discount)
    w_len = len(want)
    ans = defaultdict(int)
    for i in range(w_len):
        ans[want[i]] = number[i]
    result = 0
    for i in range(d_len-10+1):
        tmp = defaultdict(int)
        for j in range(i,i+10):
            tmp[discount[j]]+=1
        gOrStop = 0
        for ky, vl in ans.items():
            if((ky not in tmp.keys()) or tmp[ky] < vl):
                gOrStop = 1
                break
        if(gOrStop == 0):
            result+=1
    return result
            
                
                
            
        
        
        
        

    
    