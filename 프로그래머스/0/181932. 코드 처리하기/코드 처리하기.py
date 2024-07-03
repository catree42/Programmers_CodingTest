def solution(code):
    mode = 0
    ret = ''
    
    for idx, char in enumerate(code) :
            if mode == 0 :
                if code[idx] != '1' :
                    if idx%2 == 0 :
                        ret+=code[idx]
                else : 
                    mode = 1
                    
            else : 
                if code[idx] != '1' :
                    if idx%2 != 0 :
                        ret+=code[idx]
                else :
                    mode = 0
    
    
    return ret if len(ret) > 0 else "EMPTY"