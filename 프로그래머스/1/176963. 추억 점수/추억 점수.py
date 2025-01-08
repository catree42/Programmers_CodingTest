def solution(name, yearning, photo):
    
    dic = {}
    
    # 이름-추억 딕셔너리
    for i in range(len(name)) : 
        dic[name[i]] = yearning[i] 
    
    scores = []
    
    for p in photo : 
        sum = 0
        for name in p :
            try : 
                sum += dic[name]
            except :
                continue
        scores.append(sum)
    
    return scores