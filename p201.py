import sys
input = sys.stdin.readline

total = 0
def binary_search(array, start, end, target):
    result = None
    while(start <= end):
        mid = (start + end) // 2
        sum = 0
        for i in range(n-1, -1, -1):
            if(mid >= array[i]):
                break
            sum+=(array[i] - mid)
        if(sum >= target): # 이 부분에서 result 이전 값을 저장하는거 까먹지 말기
            result = mid
            start = mid+1
        else:
            end = mid-1
    return result

            
            
                

n,m = map(int, input().split())
array = list(map(int, input().split()))

array.sort()
ans = binary_search(array, 0, array[n-1], m)
print(ans)