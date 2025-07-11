import sys
input = sys.stdin.readline

def operation(e1, e2):
    elem1 = int(e1)
    elem2 = int(e2)
    if((elem1 == 0 or elem1 == 1) or (elem2 == 0 or elem2 == 1)): #부등호 써서 <=1 일때로 처리할 수도 있음
        return elem1 + elem2
    return elem1 * elem2


array = list(map(str, input().rstrip()))

elem = int(array[0])
for i in range(1,len(array)):
    elem = operation(elem, array[i])
print(elem)