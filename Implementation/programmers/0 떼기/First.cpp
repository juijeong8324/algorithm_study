#include <string>
#include <vector>

using namespace std;

string solution(string n_str) {
    int num = stoi(n_str); // int로 변환 -> 자동으로 앞의 0이 사라짐
    return to_string(num); // string으로 변환
}
