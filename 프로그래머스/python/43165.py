import sys
input = sys.stdin.readline
from collections import deque


def solution(numbers, target):
    n = len(numbers)
    q = deque()
    idx = 0
    q.append((numbers[idx], idx))
    q.append((-numbers[idx], idx))
    cnt = 0
    while(q):
        elem, idx = q.popleft()
        if(idx == n-1):
            if(target == elem):
                cnt+=1
        else:
            q.append((elem+numbers[idx+1], idx+1))
            q.append((elem-numbers[idx+1], idx+1))
        
    return cnt
                
        

numbers = [4, 1, 2, 1]
target = 4
print(solution(numbers,target))