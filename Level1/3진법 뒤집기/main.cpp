// Link : https://programmers.co.kr/learn/courses/30/lessons/68935

## 나의 방법 ##

#include <string>
#include <vector>
#include <iostream>
#include <cmath> // pow 함수 쓰기 위해서 

using namespace std;
string three(long long int m); // 함수 선언 

int solution(int n) {
    long long int answer = 0; // 들어오는 숫자가 1억까지 있어서 long long 타입으로 받기
    string s_answer = three(n); // 3진법 전환 후 반환
    int size = s_answer.size(); // 문자열 길이 받기 
    
    long temp = stol(s_answer); // 문자열을 long 타입으로 받기 
    for(int i = 0; i < size; i++){
        long long num = temp % 10; // 나머지는 자릿수가 낮은 애들부터 나온다
        temp = temp / 10;
        
        answer += num*pow(3,i); // 10진수에 바꿔서 더해주기
    }
    
    return answer;
}

string three(long long int m){ // 함수 정의
    long long int temp = m;
    string num;
    
    while(temp != 0){
        num = num + to_string(temp % 3); // 자동으로 뒤의 숫자부터 나오기 때문에 굳이 reverse() 안해도 된다!
        temp = temp / 3;
    }

    return num;
}

## 다른 사람의 풀이 ##
# Link : https://programmers.co.kr/learn/courses/30/lessons/68935/solution_groups?language=cpp

#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    vector<int> v;
    while(n > 0){
        v.push_back(n%3); // 나머지를 벡터에 저장 이때 순서는 자연스럽게 바뀜
        n/=3;
    }
    int k = 1;
    while(!v.empty()) {
        answer += k*v.back(); // 첫 번째 자리수씩(그래서 v.back) 부터 해당 원소값 * 자리수를 더해준다 
        v.pop_back(); // 맨 뒤에 있는 원소를 아예 삭제(메모리 삭제인듯)
        k*=3; // 자리수 증가에 따라 3 곱해주기
    }

    return answer;
}
