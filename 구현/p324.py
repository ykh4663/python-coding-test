import sys
input = sys.stdin.readline



def solution(s):
    n = len(s)
    tot_mn = len(s)
    for i in range(1,n//2+1):
        elem = s[:i]
        tot_cnt = 0
        cnt = 1
        for j in range(i, n, i):
            new_elem = s[j:j+i]
            if(elem == new_elem):
                cnt+=1
                continue
            else:
                if(cnt > 1):
                    tot_cnt+=(i+len(str(cnt)))
                else:
                    tot_cnt+=i
                elem = new_elem
                cnt = 1
              # 루프 끝난 뒤 마지막 덩어리 처리
        if cnt > 1:
            # 반복된 덩어리였으면 "개수+원래 길이"만큼
            tot_cnt += (i + len(str(cnt)))
        else:
        # 반복 없던 덩어리(정상 단위)나 잘린 마지막 덩어리는
           # 실제 남은 길이만큼
            tot_cnt += len(elem)
        tot_mn = min(tot_mn, tot_cnt)
    return tot_mn




s = "ababcdcdababcdcd"
rs = solution(s)
print(rs)

#hard
#p325부터 다시