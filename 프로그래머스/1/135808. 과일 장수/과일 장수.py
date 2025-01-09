def solution(k, m, score):
    
    # score 내림차순 정렬
    score.sort(reverse=True)
    
    sum = 0
    for i in range(m-1,len(score),m) : 
        sum += score[i] * m
        
    return sum