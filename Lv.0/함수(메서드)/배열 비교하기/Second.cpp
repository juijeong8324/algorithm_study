// 프로그래머스 김도현 님의 풀이 
#include <bits/stdc++.h>
using namespace std;

int solution(vector<int> arr1, vector<int> arr2) {
    if (arr1.size() != arr2.size())
        return arr1.size() > arr2.size() ? 1 : -1; // 삼항 연산자 사용 arr1.size() > arr2.size()가 True면 1, False면 -1을 반환하게 됨! 
    int sum1 = accumulate(begin(arr1), end(arr1), 0);
    int sum2 = accumulate(begin(arr2), end(arr2), 0);
    return sum1 > sum2 ? 1 : sum1 == sum2 ? 0 : -1;
}
