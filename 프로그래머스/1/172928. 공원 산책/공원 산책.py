# park = ["OOOOO", "OOOOO", "OOSOO", "OOOOO", "OOOOO"]
# routes = ["E 3", "W 3", "S 3", "N 3", "E 2", "E 1", "W 4", "W 1", "S 2", "S 1", "N 4", "N 1"]
# result = [0, 0]

# 파이썬 음수 인덱싱 조심!!

def solution(park, routes):
    
    park_list = []
    
    
    # park를 2차원 리스트로 만들기 
    for line in park :
        temp = list(line)
        park_list.append(temp)
    
    # 시작 위치 인덱스 찾기
    for i in range(len(park_list)) :
        for j in range(len(park_list[i])) :
            if park_list[i][j] == "S" :
                start = [i,j]
                continue
    
    current = start 
    
    # routes 따라서 가기
    for route in routes :
        arr = route.split(' ')
        i = current[0]
        j = current[1]
        
        try :
            count = 0 
            for _ in range(int(arr[1])) :
                count += 1 
                if arr[0] == "E" :
                    j += 1
                elif arr[0] == "W" :
                    j -= 1
                elif arr[0] == "N" :
                    i -= 1
                elif arr[0] == "S" :
                    i += 1
                # 장애물 확인 및 정상인덱스 확인 
                if park_list[i][j] == "X":
                    raise ValueError          
                if i < 0 or j < 0 :
                    raise IndexError
                
        except IndexError:
            print(f"{current} : {count} 번째에서 파크 벗어남")
            continue
        except ValueError:
            print(f"{current} : {count} 번째에서 장애물 만남")
            continue
            
        current = [i,j]
        print(f"{current} : Success")
            
    return current