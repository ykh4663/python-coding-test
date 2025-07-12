import sys
input = sys.stdin.readline

def binary_search(graph, left, right):
    while(left <= right):
        mid = (left + right) // 2
        if(graph[mid] == mid):
            return mid
        elif(graph[mid] < mid):
            left = mid+1
            #최대 인거 찾을때 mid 저장
        else:
            right = mid-1
            #최소인거 찾을 때 mid 저장
    
        
    return -1
n = int(input())
array = list(map(int, input().split()))

left , right = 0, len(array)-1
elem = binary_search(array, left, right)
print(elem)
