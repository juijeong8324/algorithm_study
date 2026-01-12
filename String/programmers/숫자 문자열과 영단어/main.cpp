#include <string>
#include <vector>

using namespace std;

int solution(string s) {
    int answer = 0;

    string num_str[] = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    int len = s.length();

    for (int i = 0; i < len; i++) {
        if (s[i]  >= '0' && s[i] <= '9') { // 숫자일 때 
            answer = answer * 10 + s[i] - '0';
        }
        else {
            for (int j = 0; j < 10; j++) {
                // 문자열일 때 
                if(!num_str[j].compare(0, num_str[j].length(), s, i, num_str[j].length())) {
                    answer = answer * 10 + j;
                }
            }

        }
    }  

    return answer;
}

/* 문자열에 1~9에 대응하는 문자열을 찾아서 대체*/
int solution(string s) {
    int answer = 0;
    vector<string> num_eng = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

    for(int i = 0; i < num_eng.size(); i++) { // 각 문자열을 순회하여
        int idx = 0;
        while((idx = s.find(num_eng[i])) != string::npos) {
            s.replace(idx, num_eng[i].size(), to_string(i)); // int 값으로 대체
        }
    }

    answer = stoi(s);

    return answer;
}