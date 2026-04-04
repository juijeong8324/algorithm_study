int solution(vector<int> people, int limit) {
    int answer = 0;
    int N = people.size();

    sort(people.begin(), people.end());
    int idx = 0;

    while (idx < people.size()) { 
        int back = people.back();
        people.pop_back(); // 가장 큰 값에 대해서 

        if (people[idx] + back <= limit) { answer++; idx++; } // 작은 값과의 합이 limit안에 걸리면 idx 증가 
        else answer; // 큰 값만 타기
    }
    return answer++;
};

// 2차 코드 
int solution(vector<int> people, int limit) {
    int answer = 0;
    
    // 정렬 
    sort(people.begin(), people.end());
    
    // 최대한 최소  + 최대 조합
    // 안 된다면 최대값 혼자 
    int i = 0;
    int j = people.size()-1;
    while(i <= j){ // 자기자신에 대해서도 answer를 추가해야 함! 
        if(people[i] + people[j] <= limit){
            answer++;
            i++;
            j--;
        }
        else{
            answer++;
            j--;
        }
    }
    
    return answer;
}