def solution(a, b, c):
    list = [a,b,c]
    count = 0
    for i in range(len(list)-1) : 
        for j in range(i+1,len(list)) :
            if list[i] == list[j] :
                count += 1
    
    if count < 1 :
        answer = a+b+c
    elif count < 2 :
        answer = (a+b+c)*(a**2 + b**2 + c**2)
    else : 
         answer = (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    
    return answer