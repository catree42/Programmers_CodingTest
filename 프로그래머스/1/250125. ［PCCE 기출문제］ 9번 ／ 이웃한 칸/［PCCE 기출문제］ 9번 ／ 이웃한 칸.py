def solution(board, h, w):
    
    color = board[h][w]
    count = 0

    try : 
        if h-1 >= 0 : 
            if board[h-1][w] == color : 
                count+=1
    except :
        pass
    try : 
        if board[h+1][w] == color:
            count+=1
    except :
        pass
    try : 
        if w-1 >= 0: 
            if board[h][w-1] == color:
                count+=1
    except :
        pass
    try : 
        if board[h][w+1] == color:
            count+=1
    except :
        pass
    
    return count