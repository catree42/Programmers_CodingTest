def solution(wallpaper):
    # 상하좌우 맨 끝 찾기
    
    left =  len(wallpaper[0]) - 1 
    right = 0
    top = len(wallpaper) - 1 
    bottom = 0
    
    mlist = [top, left, bottom, right]
    
    for i, line in enumerate(wallpaper): 
        for j, item in enumerate(line) :
            if item == "#" :
                if i < mlist[0] : 
                    mlist[0] = i
                if i+1 > mlist[2] :
                    mlist[2] = i+1
                if j < mlist[1] :
                    mlist[1] = j
                if j+1 > mlist[3] :
                    mlist[3] = j+1
                print(mlist)
    
    return mlist