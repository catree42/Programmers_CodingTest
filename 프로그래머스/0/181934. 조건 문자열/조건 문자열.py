def solution(ineq, eq, n, m):
    
    result = 0
    if ineq == '<' :
        if eq == '=' :
            result = int(n<=m)
        else :
            result = int(n<m)
    else : 
        if eq == '=' :
            result = int(n>=m)
        else :
            result = int(n>m)
    
    return result
