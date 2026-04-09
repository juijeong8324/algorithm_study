/*
    1. Input 
        - 문자열 s = 공백으로 구분된 숫자들 
    2. Output 
        "최솟값 최댓값"
*/

#include <bits/stdc++.h>
using namespace std;

string solution(string s) {
    stringstream ss(s);
    string token;
    int min_ans = INT_MAX;
    int max_ans = INT_MIN;
    
    while (ss >> token) {
        int num = stoi(token);
        min_ans = min(min_ans, num);
        max_ans = max(max_ans, num);
    }
    
    return to_string(min_ans) + " " + to_string(max_ans);
}