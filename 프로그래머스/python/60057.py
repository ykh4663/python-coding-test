def solution(s):
    l_s = len(s)
    result = l_s
    for i in range(1,l_s//2+1):
        ans = ""
        cnt = 1
        elem = s[:i]
        for j in range(i,l_s,i):
            if(elem != s[j:j+i]):
                if(cnt == 1):
                    ans+=elem
                else:
                    ans +=(str(cnt)+elem)
                if(j+i >= l_s):
                    elem = s[j:]
                else:
                    elem = s[j:j+i]
                cnt = 1
            else:
                cnt+=1
        if(cnt != 1):
            ans +=(str(cnt)+elem)
        else:
            ans+=elem
        
        local_cnt = len(ans)
        if(result > local_cnt):
            result = local_cnt
    return result
        








s = "xababcdcdababcdcd"
print(solution(s))