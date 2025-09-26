  
#include <iostream>
#include <vector>
using namespace std;

int find(vector<int> vect, int m, int tn);

int main(void) {
    vector<int> fibo; // 피보나치 수열을 담을 벡터 
    int num; // 주어진 사람 수 
    int temp; // 피보나치 다음 수 
    cin >> num;

    fibo.push_back(1);
    fibo.push_back(1);
    temp = fibo[0] + fibo[1]; // F2
    fibo.push_back(temp); // fibo에 저장
    int temp_num = 2; // F2의 2

    while (temp < num) {
        temp = temp + fibo[temp_num - 1];
        fibo.push_back(temp);
        temp_num++;
    }

    if (num == fibo[temp_num]) {
        cout << fibo[temp_num - 1] << endl;
    }
    else {
        cout << find(fibo, num, temp_num) << endl;
    }

}

int find(vector<int> vect, int m, int tn) { // 제켄도르프 정리로 피보나치킨 찾기  
    int t = vect[tn - 1]; // vect[tn]은 num보다 이미 크다
    vector<int> index; // index를 담을 애덜 
    int t_index = tn - 3; // tn-2면 tn-1과 연속하기 때문
    int answer = 0;

    index.push_back(tn - 1); 
    m -= t;

    while (m > 0) {
        if (m == vect[t_index]) {
            index.push_back(t_index);
            break;
        }
        else if (m < vect[t_index]) {
            t_index--;
        }
        else {// m > vect[t_index]
            t = vect[t_index];
            index.push_back(t_index);
            t_index -= 2;
            m -= t;
        }

    }
    for (int i = 0; i < index.size(); i++) {
        answer += vect[index[i] - 1];
    }

    return answer;


}
