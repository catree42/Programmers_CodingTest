def solution(intStrs, k, s, l):
    answer = []
    
    for string in intStrs :
        num = int(string[s:s+l]) 
        answer.append(num) if num > k else None
    return answer