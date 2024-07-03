def solution(n):
    sum = 0
    i = 1
    if n%2 == 0 :
        while i*2 <= n  :
            sum += pow(i*2,2)
            i+=1
    else :
        while i*2-1 <= n :
            sum += i*2-1
            i+=1
    return sum