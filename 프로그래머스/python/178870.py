INF = int(1e9)
def solution(sequence, k):
    ans = []
    n = len(sequence)
    start, end = 0, 0
    current_sum = sequence[0]
    min_len = INF
    while(start <= end):
        if(current_sum < k):
            if end == n - 1:
                break
            end += 1
            current_sum += sequence[end]
        elif(current_sum > k):
            current_sum -= sequence[start]
            start+=1
        else:
            if(end-start < min_len):
                min_len = end-start
                ans = [start, end]
            current_sum -= sequence[start]
            start+=1
    return ans





sequence = [1,2,3,4,5]
k = 7
result = solution(sequence, k)
print(result)