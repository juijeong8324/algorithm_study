#include <string>
#include <vector>
#include <array>

using namespace std;

vector<int> solution(vector<int> arr) {
    array<int, 11> pow = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024}; // arr의 최대 길이가 1000이므로
    int zero = 0;
    
    for(int i = 0; i < pow.size(); i++){
        if(arr.size() <= pow[i]){ // 2의 거듭제곱 값보다 크거나 같으면
            zero = pow[i] - arr.size(); // 간격을 구함 
            break;
        }
    }
    arr.insert(arr.end(), zero, 0); // arr의 마지막 원소 다음 번째 부터 0을 zero개 만큼 추가
    return arr;
}
