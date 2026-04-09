#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

/*
    - Hint
    format을 대신하는 함수가 있어..? 없어... 
    그래서 숫자 -> 이진수 -> 문자열로 변환해야 할듯
    bitset<bit 상수>(숫자 변수) = 숫자 -> 이진수 
*/

vector<int> solution(string s) {
    vector<int> answer(2, 0); // 2개를 0으로 초기화 
    
    while(s != "1"){
        int count = 0;
        int n = s.size();
        for(int i=0; i<n; i++){
            if(s[i] == '1'){
                count++;
            }        
        }
        
        s = bitset<32>(count).to_string(); // count를 32bit의 2진수로 바꾸기 -> 문자열
        s = s.substr(s.find('1'));  
        
        answer[0]++; 
        answer[1] += n - count;
    }
    
    return answer;
}