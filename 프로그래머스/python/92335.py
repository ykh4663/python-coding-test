def convert(n,k):
    ans = []
    while(n > 0):
        ans.append(str(n%k))
        n //=k
    ans.reverse()
    return ans

def isPrime(elem):
    num = int("".join(elem))
    
    if(num < 2):
        return False
    for i in range(2, int(num**0.5)+1):
        if(num % i == 0):
            return False
    return True
    

def solution(n, k):
    num = convert(n,k)
    l = len(num)
    idx = 0
    cnt = 0
    for i in range(l):
        if(num[i] == '0'):
            new_idx = i
            if(idx != new_idx):
                if(isPrime(num[idx:new_idx])):
                    cnt+=1
            idx = new_idx
        else:
            continue
    if(idx!= l-1):
        if(isPrime(num[idx:l])):
            cnt+=1

    return cnt
    
        



n = 437674
k = 3
result = solution(n,k)
print(result)