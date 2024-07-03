def solution(numLog):
    str = ''
    for idx in range(len(numLog)-1) :
        gap = numLog[idx+1] - numLog[idx]
        if gap == 1 :
            str += "w"
        elif gap == -1 :
            str += "s"
        elif gap == 10 :
            str += "d"
        elif gap == -10 :
            str += "a"
    
    return str