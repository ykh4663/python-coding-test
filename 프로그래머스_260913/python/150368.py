from itertools import product

# 예를 들어 lst = [10, 20, 30, 40] 이고 이모티콘이 4개일 때 permutations(lst, 4)를 하면:

# (10, 20, 30, 40), (40, 30, 20, 10) 등은 나오지만,

# (40, 40, 40, 40) 이나 (30, 30, 10, 20) 같은 경우는 절대 나오지 않습니다.

def convert(elem):
    if(elem == 10):
        return 0.9
    elif(elem == 20):
        return 0.8
    elif(elem == 30):
        return 0.7
    else:
        return 0.6
    

def solution(users, emoticons):
    answer = []
    discount = [10,20,30,40]
    n = len(users)
    m = len(emoticons)
    prod = list(product(discount, repeat = m))

    for p in prod:
        tmp = [0,0]
        for i in range(n):
            s = 0
            for j in range(m):
                if(users[i][0] <= p[j]):
                    #s+= emoticons[j] * ((100-p[j]) / 100)
                    s += emoticons[j] * (100 - p[j]) // 100 #조건 중 emoticons가 100의 배수라는 말이 있어 몫연산 써도 ㄱㅊ 나머지 써버리면 부등호 연산 시 이상하게 처리

            if(s >= users[i][1]):
                tmp[0] += 1
            else:
                tmp[1] += s
        answer.append(tmp)
    
    answer.sort(key = lambda x : (-x[0], -x[1]))
    return answer[0]
    


   


users = [[40, 10000], [25, 10000]]
emoticons = [7000, 9000]
result = solution(users, emoticons)
print(result)