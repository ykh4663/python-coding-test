def solution(data, col, row_begin, row_end):
    col, row_begin, row_end = col-1, row_begin-1, row_end-1
    data.sort(key = lambda x: (x[col], -x[0]))
    S_2, S_3 = 0,0
    S_2 = data[row_begin][0]%(row_begin+1) + data[row_begin][1]%(row_begin+1) + data[row_begin][2]%(row_begin+1)
    S_3 = data[row_end][0]%(row_end+1) + data[row_end][1]%(row_end+1) + data[row_end][2]%(row_end+1)

    return S_2 ^ S_3

data = [[2,2,6],[1,5,10],[4,2,9],[3,8,3]]
col = 2
row_begin = 2
row_end = 3
result = solution(data, col, row_begin, row_end)
print(result)
#특정값만 세는게 아니라 사이에 있는 값들 누적해서 XOR 해야된다