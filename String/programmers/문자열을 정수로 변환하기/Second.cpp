#include <string>
#include <vector>

using namespace std;

int solution(string n_str) {
    int answer = 0; // 반드시 0으로 초기화!
    
    for(int i=0;i<n_str.size();i++){
        answer *= 10; // 자릿수를 결정, 제일 높은 자릿수는 10^(n-1)이고, 가장 낮은 자릿수는 10^0이다. 
        answer += n_str[i]-'0'  // 각 digit을 꺼냄
    }
}
