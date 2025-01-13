def solution(id_list, report, k):
    mail_counts = {}
    # reported : repoters 
    reported_dic = {}
    
    # report 중복 제거
    report = list(set(report))
    
    for id in id_list :
        reported_dic[id] = []
        mail_counts[id] = 0
    
    for r in report :
        reporter, reported = r.split()
        reported_dic[reported].append(reporter) 
        
    
    for reported, reporters in reported_dic.items():
        if len(reporters) >= k :
            for reporter in reporters :
                mail_counts[reporter] += 1
                
    return list(mail_counts.values())