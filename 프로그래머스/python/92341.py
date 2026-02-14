from collections import defaultdict
import math

def convert_time(time):
    
    h,m = time.split(":")
    h,m = int(h), int(m)
    return h * 60 + m

def solution(fees, records):
    default_time, default_fee, per_time, per_fee = fees
    in_lst = dict()
    total = defaultdict(int)
    for r in records:
        time, car_num, sel = r.split(" ")
        min_time = convert_time(time)
        if(sel == 'IN'):
            in_lst[car_num] = min_time
        else:
            cur_time = convert_time(time)
            prev_time = in_lst.pop(car_num)
            total[car_num]+=(cur_time-prev_time)
    for k,v in in_lst.items():
        cur_time = convert_time("23:59")
        prev_time = v
        total[k] += (cur_time - prev_time)
    lst = []
    for ky, vl in total.items():
        lst.append((ky, vl))
    lst.sort()
    ans = []
    for l in lst:
        car, cum = l
        if(cum<=default_time):
            ans.append(default_fee)
        else:
            ans.append(default_fee+math.ceil((cum-default_time)/per_time)*per_fee)
    return ans

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
result = solution(fees, records)
print(result)
            
        
        
        
            
            


