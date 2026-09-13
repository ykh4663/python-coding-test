from collections import defaultdict
def solution(want, number, discount):
    answer = 0
    sl = 10
    
    n = len(number)
    bucket = defaultdict(int)
    
    for i in range(n):
        bucket[want[i]] = number[i]
    
    dlen = len(discount)
    
    for i in range(0, dlen- sl + 1):
        tmp = defaultdict(int)
        for j in range(sl):
            tmp[discount[i+j]] += 1
        if(len(bucket) != len(tmp)):
            continue
        gOrStop = 0
        for ky, vl in bucket.items():
            if ky not in tmp.keys():
                continue
            if(vl > tmp[ky]):
                gOrStop = 1
                break
        if(gOrStop == 0):
            answer+=1
    return answer

want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount =["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
print(solution(want, number, discount))