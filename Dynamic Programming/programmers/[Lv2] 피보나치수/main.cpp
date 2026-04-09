#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    vector<int> fibo(n+1, 0); // n개를 0으로 초기화 
    
    fibo[1] = 1;
    for(int i=2; i <= n; i++){
        fibo[i] = (fibo[i-2] + fibo[i-1]) % 1234567; // int 21억까지라 overflow 방지, 크기 고정 이슈..
    }
    return fibo[n] % 1234567;
}