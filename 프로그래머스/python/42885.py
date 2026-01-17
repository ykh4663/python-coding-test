from itertools import combinations
def solution(people, limit):
    people.sort()
    i,j = 0, len(people)-1
    boats = 0
    while(i <= j):
        if(people[i] + people[j] <= limit):
            i+=1
        j-=1
        boats+=1
    return boats
            
            
people = [70, 50, 80, 50]	
limit = 100
print(solution(people, limit))