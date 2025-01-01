def timeToSec(time):
    temp = time.split(':')
    min = int(temp[0])
    sec = int(temp[1])
    secs = min*60 + sec
    return secs 
    
def skip(pos_sec, op_start_sec, op_end_sec) :
    if pos_sec >= op_start_sec and pos_sec <= op_end_sec :
        pos_sec = op_end_sec
    
    return pos_sec

def solution(video_len, pos, op_start, op_end, commands):
    video_len_sec = timeToSec(video_len)
    pos_sec = timeToSec(pos)
    op_start_sec = timeToSec(op_start)
    op_end_sec = timeToSec(op_end)
    
    
        
    
    for c in commands :
        
        pos_sec = skip(pos_sec, op_start_sec, op_end_sec)
        
        if c == 'prev':
            if pos_sec < 10:
                pos_sec = 0
            else :
                pos_sec -= 10
        elif c == 'next':
            if video_len_sec - pos_sec < 10 :
                pos_sec = video_len_sec
            else :
                pos_sec += 10
            
        pos_sec = skip(pos_sec, op_start_sec, op_end_sec)
        
    pos_min = f"{int(pos_sec/60)}".zfill(2)
    pos_sec = f"{pos_sec%60}".zfill(2)
    pos = pos_min+":"+pos_sec
    
    # 기능 수행 후 시간
    return pos

