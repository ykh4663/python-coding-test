# import sys
# input = sys.stdin.readline

# n= int(input())
# coin = list(map(int, input().split()))

# coin.sort()

# elem = 0

# for c in coin:
#     if(elem + 1 >= c):
#         elem += c
#     else:
#         break
# elem+=1
# print(elem) 
#내 풀이

import sys
input = sys.stdin.readline

n= int(input())
coin = list(map(int, input().split()))

coin.sort()

target =1
for x in coin:
    if(target < x):
        break
    target += x
print(target)

#나중에 다시 한 번 풀어보기






