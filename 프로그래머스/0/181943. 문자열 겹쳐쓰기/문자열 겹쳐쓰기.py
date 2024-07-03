def solution(my_string, overwrite_string, s):
       # my_string[s:s+len(overwrite_string)] = overwrite_string
    
    myList = list(my_string)
    
    myList[s:s+len(overwrite_string)] = overwrite_string 
    
    answer = "".join(myList)
    
    return answer

# aaaaaa, bbb, 3
# 5, 3, 3