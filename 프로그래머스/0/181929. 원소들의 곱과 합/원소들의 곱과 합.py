def solution(num_list):
    product = 1
    sum = 0
    for num in num_list : 
        product *= num
        sum += num
    squaredSum = sum**2
    
    return int(product < squaredSum)