import sys
import heapq
input = sys.stdin.readline
def solution(food_times, k):
    if(sum(food_times) <= k):
        return -1
    
    q=  []
    length = len(food_times)
    previous = 0
    sum_value = 0
    for i in range(length):
        heapq.heappush(q, (food_times[i], i+1))
    while(sum_value + length * (q[0][0]-previous) <= k):
        a,b = heapq.heappop(q)
        sum_value += length * (a-previous)
        length -=1
        previous = a
    q.sort(key=lambda x : x[1])
    return q[(k-sum_value) % length][1]

    

food_times = [8,6,4]
k = 15

result = solution(food_times, k)
print(result)

#다시 풀어보기