#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;
bool comp(pair<long long, long long> a, pair<long long, long long> b);


int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    long long n;
    long long x;
    long long y;

    cin >> n;

    vector<pair<long long, long long>> v; // 변수들을 담을 컨테이너 
    vector<long long> e; // 기계의 각 종료 시간을 담을 컨테이너 

    for (long long i = 0; i < n; i++) {
        cin >> x >> y;
        v.push_back(make_pair(x, y));
    }

    sort(v.begin(), v.end(), comp); // first를 기준으로 정렬 됨

    long long j = 0;
    e.push_back(v[0].second);
    for (long long i = 1; i < v.size(); i++) {
        while (j < e.size()) { // 작동중인 모든 기계의 마지막 시간 확인! 
            if (e[j] <= v[i].first) { // 내가 틀린 부분이다... 아니... 종료시간이랑 시작 시간 같아도 되는 거였자나... a, b-1 시간으로 생각하자!! 
                e[j] = v[i].second; // 업데이트
                break; // 끝
            }
            j++;
        }
        if (j == e.size()) {
            e.push_back(v[i].second);
        }
      
        j = 0;
    }

    cout << e.size();
}
bool comp(pair<long long, long long> a, pair<long long, long long> b) {
    if (a.first < b.first) return true;
    else if (a.first == b.first) {
        if (a.second < b.second) {
            return true;
        }
        else {
            return false;
        }
    }
    else {
        return false;
    }
    return false; // return 값은 항상 써주기를... 
}
