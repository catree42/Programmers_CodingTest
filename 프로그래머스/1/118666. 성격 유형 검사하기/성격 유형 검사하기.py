def solution(survey, choices):
    personality_dic = {"RT":0,"CF":0,"JM":0,"AN":0}
    
    score_dic = {} 
    min = -3 
    for i in range(1,8) :
        score_dic[i] = min
        min += 1
    
    for i in range(len(survey)) :
        try :
            personality_dic[survey[i]] += score_dic[choices[i]]
        except :
            personality = survey[i][1]+survey[i][0]
            personality_dic[personality] -= score_dic[choices[i]]
    
    result = ""
    
    for key, value in personality_dic.items() :
        if value <= 0 : 
            result += key[0]
        elif value > 0:
            result += key[1]

    return result