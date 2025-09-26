// 프로그래머스 '한창균'님의 풀이 과정
#include <string>
#include <vector>
#include <cmath>
using namespace std;

vector<int> solution(vector<int> arr) {
    int n = arr.size();
    int dst = pow(2, ceil(log2(n))); // 예를 들어 n=6이면 (2 < 루트 6 < 3) 이므로 ceil(6)=3

    for(int t = 0; t < dst - n; ++t)
    {
        arr.push_back(0);
    }

    return arr;
}
