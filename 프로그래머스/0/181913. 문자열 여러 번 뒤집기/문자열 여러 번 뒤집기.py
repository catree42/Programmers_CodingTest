def solution(my_string, queries):
    strList = [char for char in my_string] 
    
    for query in queries :
        s = query[0]
        e = query[1]    
        reverse_s = s - len(strList) # 0 -> -11
        reverse_e = e - len(strList) # 10 -> -1
        #string1 = my_string[s:e+1] if e < len(my_string)-1 else my_string[s:]
        # my_string[s:e+1] = my_string[s:e+1:-1]
        #my_string = my_string.replace(my_string[s:e+1],my_string[reverse_e:reverse_s-1:-1])
        strList[s:e+1] = strList[reverse_e:reverse_s-1:-1]
    return "".join(strList)