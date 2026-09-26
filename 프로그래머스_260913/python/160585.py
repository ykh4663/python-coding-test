n = 3
def bingo(graph, elem):
    #가로로 빙고 있는지 확인
    for i in range(n):
        gOrStop = 0
        for j in range(n):
            if(graph[i][j] != elem):
                gOrStop = 1
                break
        if(gOrStop == 0):
            return True
    #새로로 잘되는지
    for j in range(n):
        gOrStop = 0
        for i in range(n):
            if(graph[i][j] != elem):
                gOrStop = 1
                break
        if(gOrStop == 0):
            return True
    #대각선으로 잘되는지(0,0 1,1 2,2)
    gOrStop = 0
    for i in range(n):
        if(graph[i][i] != elem):
            gOrStop = 1
            break
    if(gOrStop == 0):
        return True
    
    #대각선으로 잘되는지(2,0 1,1 0,2)
    gOrStop = 0
    for i in range(n):
        if(graph[n-i-1][i] != elem):
            gOrStop = 1
            break
    if(gOrStop == 0):
        return True
    
    
    return False

                
        

def solution(board):
    oCnt, xCnt = 0,0
    for i in range(n):
        for j in range(n):
            if(board[i][j] == 'O'):
                oCnt+=1
            elif(board[i][j] == 'X'):
                xCnt+=1
    
            
    first_bingo = bingo(board, 'O')
    last_bingo = bingo(board, 'X')
    
    
    if(oCnt - xCnt != 1 and oCnt - xCnt != 0): # 빙고가 만들어지더라도 해당 조건 만족안하면 안됨
        return 0

    if(first_bingo):
        if(oCnt <= xCnt):
            return 0

    if(last_bingo):
        if(oCnt != xCnt):
            return 0
    
    return 1
    