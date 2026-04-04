#시간 분을 분으로 환산
def convert(elem):
    hour, min = elem.split(":")
    hour, min = int(hour), int(min)
    return hour * 60 + min

def isPossible(r,s,e):
    for i in range(s,e+1):
        if(r[i] == 1):
            return False
    return True
def add_time(r,s,e):
    for i in range(s,e):
        r[i] = 1

def solution(book_time):
    rooms = []
    book_time.sort(key = lambda x : x[0]) #정렬을 할 때 노는 방이 없이 가장 효율적으로 방을 쓸 수 있다
    for b in book_time:
        s, e = b[0], b[1]
        s = convert(s)
        e = convert(e)
        gOrStop = 0
        if(e + 10 >= 1440):
            e = 1439
        else:
            e += 10
        for r in rooms:
            if(isPossible(r, s, e)):
                add_time(r,s,e)
                gOrStop = 1
                break
        if(gOrStop == 0):
            time = [0] * 1440
            add_time(time, s, e)
            rooms.append(time)


    return len(rooms)
        
    






book_time = [["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]
print(solution(book_time))
