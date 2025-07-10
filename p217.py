import sys
input = sys.stdin.readline
INF = int(1e9)
x = int(input())

array = [INF] * 30001
array[1] = 0 
for i in range(2,x+1):
    array[i] = array[i-1] + 1
    if(i % 5 == 0):
        array[i] = min(array[i], array[i//5] + 1)
    if(i % 3 == 0):
        array[i] = min(array[i], array[i//3] + 1)
    if(i % 2 == 0):
        array[i] = min(array[i], array[i//2] + 1)
    
print(array[x])

