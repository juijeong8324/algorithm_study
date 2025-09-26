#include <bits/stdc++.h>

using namespace std;

int solution(vector<string> strArr) {
    array <int, 31> count{0, }; // 0으로 초기화 
    int answer = 0;
    
    for(int i=1; i <= 30; i++){ // 각 문자열의 길이 순환
        for(auto a : strArr){ // strArr에 해당하는 문자열의 길이의 원소가 있는지 체크
            if(a.size() == i) count[i] += 1;
        }
        
        answer = max(answer, count[i]); // max 체크
    }
    
    return answer;
}
