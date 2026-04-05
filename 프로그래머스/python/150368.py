from itertools import product

def make_perm_lst(l, users):#꼭 10~40 다 넣어놓고 돌릴 필요는 없음
    mn = int(1e9)
    for i in range(l):
        mn = min(users[i][0], mn)
    if(mn >= 40):
        return [40]
    elif(mn >= 30):
        return [30,40]
    elif(mn >= 20):
        return [20,30,40]
    else:
        return [10,20,30,40]



def solution(users, emoticons):
    u_len = len(users)
    lst = make_perm_lst(u_len, users)
    ans = [0, 0]
    e_len = len(emoticons)
    perm = list(product(lst, repeat=e_len))#이거 permutations 했어서 틀렸음, [40,40] 이런 값들을 불러오지 못하는 오류
    #perm 값들에 대응해서 각각 상품들의 할인 수치임
    
    for p in perm:
        local_price = [0] * u_len
        local_plus = 0
        local_tot_price = 0
        #상품들 각각의 할인수치
        for pi in range(len(p)):
            for i in range(u_len):
                if(users[i][0]<=p[pi]):
                    local_price[i] += emoticons[pi] * (100-p[pi]) // 100 # 나눗셈 해버리면 정수에서 소수로 반환되어 원하는 값 안나올 수 있으므로, 우선 곱하기 하고 최종적으로 몫연산자 하기
                else:
                    continue
        for i in range(u_len):
            if(local_price[i] >= users[i][1]):
                local_plus +=1
            else:
                local_tot_price += local_price[i]
        if(ans[0] < local_plus):
            ans[0], ans[1] = local_plus, local_tot_price
        elif(ans[0] == local_plus):
            if(ans[1] < local_tot_price):
                ans[1] = local_tot_price
    return ans
                
                
            
            
users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600, 4900]
result = solution(users, emoticons)
print(result)
    