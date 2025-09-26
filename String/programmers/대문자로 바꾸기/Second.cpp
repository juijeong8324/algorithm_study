// 아스키 코드 값 이용 
#include <string>
#include <vector>

using namespace std;

string solution(string myString) {
    for(int i=0; i< myString.length(); i++){
        if(myString[i] >= 'a'){ // 소문자인 경우만 변환
            myString[i] -= 32 ;
        }
    }
    return myString;
}
