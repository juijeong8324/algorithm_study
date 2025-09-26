#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr, int n) {
    if(arr.size() % 2 == 0){ // 짝수인 경우
        for(int i = 1; i < arr.size(); i=i+2){ // 홀수 번째
            arr[i] += n;
        }
    }else{ // 홀수인 경우 
        for(int i = 0; i < arr.size(); i=i+2){ // 짝수 번째
            arr[i] += n;
        }
    }
    return arr;
}

// 다른 사람의 풀이
#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr, int n) {

    for(int i=(arr.size()+1)%2;i<arr.size();i+=2) // arr.size()가 짝수 인 경우 홀수번째(1번째부터), arr.size()가 홀수 인 경우 짝수 번째(0번째부터)
        arr[i] += n;
    return arr;
}
