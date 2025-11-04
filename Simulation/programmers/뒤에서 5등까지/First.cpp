#include <string>
#include <algorithm> // sort()를 위해서
#include <vector>

using namespace std;

vector<int> solution(vector<int> num_list) {
    vector<int> answer;
    
    sort(num_list.begin(), num_list.end()); // default 오름차순
    
    for(int i=0; i<5; i++){
        answer.push_back(num_list[i]);
    }
    return answer;
}
