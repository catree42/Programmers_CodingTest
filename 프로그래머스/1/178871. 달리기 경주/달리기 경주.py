def solution(players, callings):
    name_dic = {}
    rank_dic = {}
    
    for idx, name in enumerate(players) : 
        name_dic[idx] = name 
        rank_dic[name] = idx 
    
    
    for idx, name in enumerate(callings) :
        current_rank = rank_dic[name]
        previous_player = name_dic[current_rank-1]
        
        name_dic[current_rank-1] = name
        name_dic[current_rank] = previous_player
        
        rank_dic[name] = current_rank-1
        rank_dic[previous_player] = current_rank
        
    # 시간 초과 : 시간복잡도 = n^2
    # for c in callings : 
    #     for i in range(len(result)) : 
    #          if c == result[i] :
    #                 temp = result[i]
    #                 result[i] = result[i-1]
    #                 result[i-1] = temp
        
    result = []
    
    for i in range(len(name_dic)) : 
        result.append(name_dic[i])
    
    
    return result