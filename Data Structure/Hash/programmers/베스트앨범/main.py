from collections import defaultdict
import heapq

def solution(genres, plays):
    answer = []
    genres_play = defaultdict(int) # 장르별 총 횟수 
    genres_list = defaultdict(list) # 장르별 최대 노래, dict의 value type은 heapq (list)
    
    # 기존 정보 저장 
    for idx, (genre, play) in enumerate(zip(genres, plays)): 
        genres_play[genre] += play # 총 재생 횟수 
        heapq.heappush(genres_list[genre], (-play, idx)); # list, 추가할 value
    
    # 베스트 앨범 추가 
    new_dict = sorted(genres_play.items(), key=lambda x: x[1], reverse=True)
    
    for genre, play in new_dict:
        for _ in range(2):
            if genres_list[genre]:
                _, idx = heapq.heappop(genres_list[genre])
                answer.append(idx)
    
    return answer