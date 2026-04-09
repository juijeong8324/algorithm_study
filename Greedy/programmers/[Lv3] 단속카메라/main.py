
def solution(routes):
    answer = 0
    last_camera = float('-inf')
    routes.sort(key = lambda x: x[1])
    
    for start, end in routes:
        if start > last_camera: # 현재 차량의 진입점이 진출점 후라면 
            last_camera = end 
            answer += 1 # 새로운 카메라 추가 
            
    return answer