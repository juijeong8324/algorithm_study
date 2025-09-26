#include <string>
#include <vector>

using namespace std;

string solution(string n_str) {
    int offset = 0;
    for(int i=0; i < n_str.size(); i++){
        if(n_str[i] == '0'){
            offset += 1; 
        } 
        else{ // 가장 왼쪽의 0이 아니므로 for문 나오기
            break;
        }
    }
    
    return n_str.substr(offset); // offset 번째 부터 자르기 
}
