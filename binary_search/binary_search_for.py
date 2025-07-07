import sys
input = sys.stdin.readline

def binary_search(array, start, end, target):
    mid = None
    while(start <= end):
        mid = (start + end) //2
        if(array[mid] == target):
            break
        elif(array[mid] > target):
            end = mid-1
        else:
            start = mid+1
    return mid



n,target = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
idx = binary_search(array, 0, n-1, target)
print(idx+1)