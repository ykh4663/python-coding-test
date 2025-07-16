import sys
input = sys.stdin.readline

INF = int(1e10)

def operate(a, i, b):
    if(i == 0):
        return a + b
    elif(i == 1):
        return a-b
    elif(i == 2):
        return a * b
    else:
        return int(a/b)

def dfs(rs, op, idx):
    global mx, mn
    if(idx== n):
        mn = min(rs, mn)
        mx = max(rs, mx)
        return
    for i in range(4):
        if(op[i] > 0):
            new_rs = operate(rs, i, elem[idx])
            op[i]-=1
            dfs(new_rs, op, idx+1)
            op[i]+=1
    

    

        


n = int(input())
elem = list(map(int, input().split()))
op = list(map(int, input().split()))
mx, mn = -INF, INF
dfs(elem[0], op, 1)
print(mx)
print(mn)


