# [[0, 4, 2]
# 0<= i <= 4 and i<=2  


 
def solution(arr, queries):
    answer = []
    
    for idx, query in enumerate(queries) :
        s, e, k = query[0], query[1], query[2]
        nums = []
        for i in range(s, e+1) :
            if arr[i] > k :
                nums.append(arr[i])
        if nums : 
            answer.append(min(nums))
        else :
            answer.append(-1)
                      
        
    return answer