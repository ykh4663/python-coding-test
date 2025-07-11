import sys
input = sys.stdin.readline

arr = list(map(str, input().rstrip()))
sum = 0
alpha = []
for a in arr:
    if('0'<=a<='9'):
        sum+=int(a)
    else:
        alpha.append(a)
alpha.sort()
if(sum != 0):
    alpha.append(sum)
for a in alpha:
    print(a,end='')