homies_mineral = [[1,1,1],[5,1,1],[25,5,1]]#각 행 열 별 0은 다이아 1은 철 2는 돌

def convert_minerals_to_idx(elem):
    if(elem == "diamond"):
        return 0
    elif(elem == "iron"):
        return 1
    else:
        return 2
def find_best_pick(picks):
    for i in range(3):
        if(picks[i] > 0):
            picks[i] -=1
            return i
    return -1
def solution(picks, minerals):
    max_mine = sum(picks) * 5
    minerals = minerals[:max_mine]
    m_len = len(minerals)
    idx=  -1
    for i in range(len(picks)-1, -1, -1):
        if(picks[i] > 0):
            idx= i
            break
    idxes = []
    for i in range(0,m_len,5):
        local_minerals = []
        local_minerals = minerals[i:i+5]
        local_len = len(local_minerals)
        total = 0
        for j in range(local_len):
            to_idx = convert_minerals_to_idx(local_minerals[j])
            total += homies_mineral[idx][to_idx]
        idxes.append((total, i))
    idxes.sort(reverse=True)
    ans = 0
    for ids in idxes:
        loc_tot, loc_id = ids
        from_idx = find_best_pick(picks)
        
        for i in range(loc_id, loc_id + 5):
            if(i >= m_len):
                break
            to_idx = convert_minerals_to_idx(minerals[i])
            ans += homies_mineral[from_idx][to_idx]
    return ans
            



            
        


    



picks = [0, 1, 1]
minerals = ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]
result = solution(picks, minerals)
print(result)
