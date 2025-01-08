def dateToInt(date : str) :
        date_list = [int(n) for n in date.split(".")]
        return date_list 

def solution(today, terms, privacies):
      
    LAST_MONTH = 12
    FIRST_DAY = 1 
    
    today_list = dateToInt(today)

    terms_dic = {}
    for term in terms :
        temp = term.split(" ")
        terms_dic[temp[0]] = int(temp[1])
    
    # 마감할 리스트 
    expire_list = []
        
    for idx, privacy in enumerate(privacies) : 
        
        date, term = privacy.split(" ")
        date_list = dateToInt(date)
        
        # 개인정보 마감일 계산
        expire_date = date_list.copy()
        expire_date[1] += terms_dic[term]
        expire_date[2] -= 1
        
        if expire_date[2] < FIRST_DAY :
            expire_date[1] -= 1
            expire_date[2] = 28
        
        if expire_date[1] < 1 :
            expire_date[0] -= 1
            expire_date[1] = 12
        
        if expire_date[1] > LAST_MONTH :
            expire_date[0] += 1
            expire_date[1] -= 12
            
        isOver = False 
        
        today_days = today_list[2] + today_list[1]*28 + today_list[0]*12*28
        expire_days = expire_date[2] + expire_date[1]*28 + expire_date[0]*12*28
        
        print(f"today:{today_days} : expire:{expire_days}")
        
        if today_days > expire_days : 
            expire_list.append(idx+1)
    
    return expire_list