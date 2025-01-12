def solution(s, skip, index):
    
    alphabet_dict= {}
    idx_dict = {}
    alphabet_list = [chr(x) for x in range(97, 123)]
    skip_idx = []

    # skip에 해당하는 인덱스
    for i in range(len(alphabet_list)) :
        for j in range(len(skip)) :
            if alphabet_list[i] == skip[j] : 
                skip_idx.append(i)
                continue
    
    # 알파벳 리스트 뒤에서부터 skip 없애기
    for idx in reversed(skip_idx) :
        alphabet_list.pop(idx)
    
    # 딕셔너리 만들기
    for i,c in enumerate(alphabet_list) :
        alphabet_dict[i] = c
        idx_dict[c] = i
    
    print(alphabet_dict)
    print(idx_dict)
    
    slist = list(s)
    # 리스트 길이로 나머지 연산해서 인덱스 범위 넘어가는 값 순환시키기
    for i, s in enumerate(slist) : 
        skip_idx = (idx_dict[s]+index) % len(alphabet_list)
        slist[i] = alphabet_dict[skip_idx]
    
    result = "".join(slist)
    
    return result
