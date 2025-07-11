import sys
input = sys.stdin.readline

array = list(map(str, input().rstrip()))

cnt = [0] * 2
elem = array[0]
for i in range(1, len(array)):
    if(elem != array[i]):
        idx = int(elem)
        cnt[idx]+=1
        elem = array[i]
    
cnt[int(elem)]+=1
print(min(cnt[0], cnt[1]))
