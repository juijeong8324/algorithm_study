// insert 함수 사용
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> num_list) {
    vector<int> answer;

    sort(num_list.begin(),num_list.end());
    answer.insert(answer.end(),num_list.begin(),num_list.begin()+ 5); // insert(answer 마지막 위치, num_list 시작 위치, num_list 시작 + 5) 

    return answer;
}
