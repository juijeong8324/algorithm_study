// 프로그래머스 sapee님의 풀이과정
#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr) {
    int a = arr.size();
    int k = 1; 
  
    while(k<a) k*=2; // arr.size() 보다 2의 거듭제곱이 더 클 때까지 2를 곱함
    for(int i=a; i<k; i++)arr.push_back(0);
    return arr;
}
