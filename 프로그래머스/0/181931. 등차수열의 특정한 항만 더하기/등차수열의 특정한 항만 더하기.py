def solution(a, d, included):
    terms = []
    for i in range(len(included)) : 
        terms.append(a+d*i)
        
    sum = 0
    for idx, term in enumerate(terms) : 
        sum += term if included[idx] else 0
    return sum