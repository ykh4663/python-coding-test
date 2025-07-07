import sys
input = sys.stdin.readline

def binary_search(array, start, end, target):
    mid = (start + end)//2
    if(array[mid] == target):
        return mid
    elif(array[mid] > target):
        return binary_search(array, start, mid-1, target)
    else:
         
        return binary_search(array, mid+1, end, target)
n,target = map(int, input().split())
array = list(map(int, input().split()))
idx = binary_search(array, 0, n-1, target)
print(idx+1)
