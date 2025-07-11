import sys
input = sys.stdin.readline

array = list(map(int,input().rstrip()))
n = len(array)
if(sum(array[:n//2]) == sum(array[n//2:])):
    print("LUCKY")
else:
    print("READY")