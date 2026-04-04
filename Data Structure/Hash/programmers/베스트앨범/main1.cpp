#include <bits/stdc++.h>

using namespace std;

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer; // 정답 
    unordered_map<string, int> genre_play; // key로 정렬 x, 기본으로 없는 key에 대해 자동 생성
    unordered_map<string, vector<pair<int, int>>> genre_list; // value는 (play 횟수, 고유번호)
    
    // genre 별 총 play 횟수 저장  
    // genre 별 각 곡의 paly 횟수 저장
    int N = genres.size();
    for(int idx=0; idx < N; idx++){
        genre_play[genres[idx]] += plays[idx];
        genre_list[genres[idx]].push_back({plays[idx], idx});
    }
    
    // genre 별 총 play 횟수 정렬
    vector<pair<string, int>> sorted_play(genre_play.begin(), genre_play.end()); // c++에서 sort는 오직 vector만 가능!!
    sort(sorted_play.begin(), sorted_play.end(), [](auto& a, auto& b){
        return a.second > b.second;
    });
    
    // genre 별 각 곡의 베스트 앨범
    for(auto item: sorted_play){
        string genre = item.first;
        
        // play 횟수를 기준으로 내림차순 정렬, 어차피 idx는 오름차순으로 추가되므로  
        sort(genre_list[genre].begin(), genre_list[genre].end(), [](auto& a, auto& b){
            return a.first > b.first;
        });
        
        int count = 0;
        for (auto& [play, idx] : genre_list[genre]) {
            if (count >= 2) break;
            answer.push_back(idx);
            count++;
        }
    }
    
    return answer;
}