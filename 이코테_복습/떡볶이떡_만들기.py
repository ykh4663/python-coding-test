def check(lst, mid):
    ret = 0
    for l in lst:
        if(mid < l):
            ret +=(l-mid)
    return ret


n,m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
start, end = 0, lst[-1]
ans = 0
while(start <= end):
    mid = (start + end) // 2
    m_elem = check(lst, mid)
    if(m_elem < m):
        end = mid-1
    else:
        ans = max(ans, mid)
        start = mid+1
print(ans)
