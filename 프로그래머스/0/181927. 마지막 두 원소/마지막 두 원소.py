def solution(num_list):
    lastIndex = len(num_list)-1
    item = 0
    
    if num_list[lastIndex] > num_list[lastIndex-1] :
        item = num_list[lastIndex] - num_list[lastIndex-1]
    else :
        item = num_list[lastIndex] * 2
    
    num_list.append(item)
    
    return num_list