def solution(s, skip, index):
    
    alphabet_dict= {}
    idx_dict = {}
    alphabet_list = [chr(x) for x in range(97, 123)]
    skip_idx = []

    for i in range(len(alphabet_list)) :
        for j in range(len(skip)) :
            if alphabet_list[i] == skip[j] : 
                skip_idx.append(i)
                continue
    
    
    for idx in reversed(skip_idx) :
        alphabet_list.pop(idx)
    
    
    for i,c in enumerate(alphabet_list) :
        alphabet_dict[i] = c
        idx_dict[c] = i
    
    print(alphabet_dict)
    print(idx_dict)
    
    slist = list(s)
    for i, s in enumerate(slist) : 
        skip_idx = (idx_dict[s]+index) % len(alphabet_list)
        slist[i] = alphabet_dict[skip_idx]
    
    result = "".join(slist)
    
    return result
