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