#include <string>
#include <vector>

using namespace std;

string solution(string myString) {
    for(int i=0; i< myString.length(); i++){
        if(myString[i] >= 'a'){ // 소문자인 경우만 변환
            myString[i] = myString[i]-'a'+'A'; // 'a'와의 간격을 파악한 후 대문자로 변환
        }
    }
    return myString;
}
