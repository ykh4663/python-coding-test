import sys

dx = [(0,0,0),(1,1,1),(2,2,2),(0,1,2),(0,1,2),(0,1,2),(0,1,2),(0,1,2)]
dy = [(0,1,2),(0,1,2),(0,1,2),(0,0,0),(1,1,1),(2,2,2),(0,1,2),(2,1,0)]

def check_O(board):
    l = len(dx)
    for i in range(l):
        gOrStop = 0
        tmp_x = dx[i]
        tmp_y = dy[i]
        elem = board[tmp_x[0]][tmp_y[0]]
        if(not elem == 'O'):
            continue
        for j in range(1,3):
            if(elem != board[tmp_x[j]][tmp_y[j]]):
                gOrStop = 1
                break
        if(gOrStop == 0):
            return False
    return True
            
def check_X(board):
    l = len(dx)
    for i in range(l):
        gOrStop = 0
        tmp_x = dx[i]
        tmp_y = dy[i]
        elem = board[tmp_x[0]][tmp_y[0]]
        if(not elem == 'X'):
            continue
        for j in range(1,3):
            if(elem != board[tmp_x[j]][tmp_y[j]]):
                gOrStop = 1
                break
        if(gOrStop == 0):
            return False
    return True
            


def solution(board):
    full_board = "".join(board)
    O_len = full_board.count('O')
    X_len = full_board.count('X')
    if(abs(O_len - X_len) > 1):
        return 0
    if(O_len < X_len):
        return 0
    if((O_len == X_len and not check_O(board)) or (O_len > X_len and not check_X(board))) :
        return 0
    return 1
    

board = ["...", ".X.", "..."]
print(solution(board))

