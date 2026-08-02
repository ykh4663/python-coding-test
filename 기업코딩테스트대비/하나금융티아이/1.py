def solution(n):
    cnt = 0
    coin_types = [500,100,50,10]
    for coin in coin_types:
        cnt += n // coin
        n %= coin


    return cnt


n = int(input())
print(solution(n))

