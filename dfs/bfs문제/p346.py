import sys
from collections import deque
input = sys.stdin.readline

def balance(p):
    lst = [0] * 2
    idx = 0
    for i in range(len(p)):
        if(p[i] == '('):
            lst[0]+=1
        else:
            lst[1]+=1
        if(lst[0] == lst[1]):
            idx = i+1
            break
    return p[:idx], p[idx:]
           
def right(u):
    q = deque()
    if(u[0] == ')'):
        return False
    else:
        q.append(u[0])
    idx = 1
    while idx <= len(u)-1:
        if(u[idx] == '('):
            q.append(u[idx])
        else:
            if(len(q) == 0):
                return False
            q.pop()
        idx+=1
    if(len(q) != 0):
        return False
    return True
def reverse(p):
    rs = []
    for i in range(len(p)):
        if(p[i] == '('):
            rs.append(')')
        else:
            rs.append('(')
    return rs

def change(u):
    ans = u[1:-1]
    return ''.join(reverse(ans))
    



def solution(p):
    
    if(len(p) == 0):
        return p
    u,v = balance(p)
    if(right(u) ==True):
        return u + solution(v)
    else:
        return "(" + solution(v) + ")" + change(u)




p = "()))((()"
ans = solution(p)
print(ans)