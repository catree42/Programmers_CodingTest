def solution(n, m, section):
    
    head = 0
    count = 0
    
    for wall in section :
        if wall > head : 
            head = wall + m-1
            count += 1 
        else : 
            continue
            
    return count