from collections import defaultdict



s = list(map(str, input().rstrip()))
dct = defaultdict(int)

s_len = len(s)
for i in range(s_len):
    elem = s[i]
    if(elem.islower()):
        elem = elem.upper()
    dct[elem]+=1
mx = -1
mx_word = ''
for ky, vl in dct.items():
    if(mx < vl):
        mx = vl
        mx_word = ky
cnt = 0
for ky, vl in dct.items():
    if(vl == mx):
        cnt+=1
if(cnt == 1):
    print(mx_word)
else:
    print("?")


