import sys
from collections import defaultdict

def check(sentence):
    prev = 0
    dct = defaultdict(int)
    sentence_len = len(sentence)
    for i in range(sentence_len):
        if(prev != sentence[i]):
            if(dct[sentence[i]] == 0):
                dct[sentence[i]]+=1
                prev = sentence[i]
            else:
                return 0
        else:
            dct[sentence[i]]+=1
    return 1
    


        

n = int(input())
cnt = 0
for _ in range(n):
    sentence = list(map(str, input().rstrip()))
    cnt+=check(sentence)
print(cnt)
