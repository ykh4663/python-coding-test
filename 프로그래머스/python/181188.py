#컨셉: 그리디 알고리즘
#우선 끝값으로 정렬하고 현재 타겟 값이 다음 시작값보다 작거나 같으면 값 갱신 후 ans 값 1 증가시키기

def solution(targets):
    targets.sort(key = lambda x: x[1])
    ans = 0
    target = 0
    for i in range(len(targets)):
        if(target<= targets[i][0]):
            target = targets[i][1]
            ans+=1
    return ans



targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
print(solution(targets))


