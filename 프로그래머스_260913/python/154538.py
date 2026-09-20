def solution(x, y, n):
    if(x == y): # 값이 같을 경우 바로 리턴(그냥 그 자체로 도달한 것이므로)
        return 0
    lst = [-1] * (y+1) # visit을 써도되고 -1로 나처럼 구현해도 될듯
    lst[x] = 0 # 처음 수는 0으로 초기화
    for i in range(x,y+1):
        if(i - n >= 0 and lst[i - n] != -1): # 음수 나올수도 있어서 >=0 체크
            if(lst[i] == -1):
                lst[i] = lst[i-n] + 1
            else:
                lst[i] = min(lst[i], lst[i-n] + 1)
        if(i % 2 == 0 and lst[i // 2] != -1):
            if(lst[i] == -1):
                lst[i] = lst[i // 2] + 1
            else:
                lst[i] = min(lst[i], lst[i // 2] + 1)
        if(i % 3 == 0 and lst[i // 3] != -1):
            if(lst[i] == -1):
                lst[i] = lst[i // 3] + 1
            else:
                lst[i] = min(lst[i], lst[i // 3] + 1)
    
    if(lst[y] == 0):
        return -1
    else:
        return lst[y]

x = 10
y = 10
n = 5
result = solution(x,y,n)
print(result)
    
        