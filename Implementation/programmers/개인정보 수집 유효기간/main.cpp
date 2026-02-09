#include <bits/stdc++.h>

using namespace std;

int t[26]; // 유효기간 
vector<int> solution(string today, vector<string> terms, vector<string> privacies) {
    vector<int> answer;
    int year = stoi(today.substr(0, 4));
    int month = stoi(today.substr(5, 2));
    int day = stoi(today.substr(8, 2));
    
    for(int i=0; i < terms.size(); i++){
        int idx = terms[i][0] - 'A'; 
        t[idx] = stoi(terms[i].substr(terms[i].find(" ")+1)); // 공백기준 문자열 자르기 
    }
    
    for(int i=0; i < privacies.size(); i++){
        int y = stoi(privacies[i].substr(0, 4));
        int m = stoi(privacies[i].substr(5, 2));
        int d = stoi(privacies[i].substr(8, 2));
        char idx = privacies[i][privacies[i].size() - 1];
        int term = t[idx-'A'];
        
         m += term;
        if(m > 12){  // 12월 이상 월이 나오면 
            y += m / 12; // 1년이 넘어감 
            m %= 12;
            if(m == 0){ // 추가한 부분
                m = 12;
                y--;
            } 
        }
        
        cout << y << " " << m << " " << d << "\n";
        if(y > year) continue; 
        if(y == year && m > month) continue;
        if(y == year && m == month && d > day) continue;
        answer.push_back(i+1);
    }
    
    return answer;
}

/* 다른 풀이 - 년도 처리 안 하고 일수로 처리 */
using namespace std;
vector<int> solution(string today, vector<string> terms, vector<string> privacies) {
    vector<int> answer;
    int year = stoi(today.substr(0, 4));
    int month = stoi(today.substr(5, 2));
    int days = stoi(today.substr(8));
    int todayD = (year)*12 * 28 + (month - 1) * 28 + days;

    vector<int> ar(privacies.size());
    map<char, int> mp;
    for (int i = 0; i < terms.size(); i++) {
        stringstream ss(terms[i]);
        char c;
        int month;
        ss >> c >> month;
        mp[c] = month;
    }
    for (int i = 0; i < privacies.size(); i++) {
        int y = stoi(privacies[i].substr(0, 4));
        int m = stoi(privacies[i].substr(5, 2));
        int d = stoi(privacies[i].substr(8, 2));
        char c = privacies[i].back();
        ar[i] = (y)*12 * 28 + (m - 1) * 28 + d + mp[c] * 28 - 1;
    }
    for (int i = 0; i < ar.size(); i++) {
        if (ar[i] < todayD) {
            answer.push_back(i + 1);
        }
    }
    return answer;
}