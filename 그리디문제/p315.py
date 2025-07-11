import sys
from itertools import combinations
input = sys.stdin.readline

n,m= map(int, input().split())
weight = list(map(int, input().split()))
lst = []
for i in range(n):
    lst.append(i)
    
lst = list(combinations(lst, 2))
cnt = 0
for c in lst:
    c1, c2 = c
    if(weight[c1] != weight[c2]):
        cnt+=1

print(cnt)


