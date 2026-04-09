#include <string>
#include <vector>

using namespace std;

int solution(string num_str) {
    int answer = 0;
    
    for(int i = 0; i<num_str.size(); i++){
        answer += num_str[i]-'0'; // 해당 자릿수에 '0'(48)을 빼서 실제 숫자로 변환 
    }
    return answer;
}
