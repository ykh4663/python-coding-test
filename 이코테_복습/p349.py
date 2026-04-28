import sys

def dfs(lst, elem, idx, plus, minus, mul, div):
    global mx, mn
    if(idx == len(lst)):#틀린부분1 lst의 len -1을 하면 안됨
        mx = max(mx, elem)
        mn = min(mn, elem)
        return#틀린부분 2 다 계산했으면 리턴 -> 리턴하던지 아래 로직을 else로 묶던지 중에 선택
        
    if(plus > 0):
        plus-=1
        dfs(lst, elem + lst[idx], idx+1, plus, minus, mul, div)
        plus+=1
    if(minus > 0):#틀린부분 3 elif로 하는게 아니라 if문으로 연결
        minus-=1
        dfs(lst, elem - lst[idx], idx+1, plus, minus, mul, div)
        minus+=1
    if(mul > 0):
        mul-=1
        dfs(lst, elem * lst[idx], idx+1, plus, minus, mul, div)
        mul+=1
    if(div > 0):# 틀린부분 4 계산할 때 그냥 나누기하고 int 씌우기
        div -=1
        dfs(lst, int(elem / lst[idx]), idx+1, plus, minus, mul, div)
        div+=1


n = int(input())
lst = list(map(int, input().split()))
op = list(map(int, input().split()))
mx = -int(1e9)
mn=  int(1e9)
#값, 인덱스, +, -, *, //
dfs(lst, lst[0], 1, op[0], op[1], op[2], op[3])
print(mx)
print(mn)