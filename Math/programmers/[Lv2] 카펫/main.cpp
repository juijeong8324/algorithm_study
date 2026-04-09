#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    
    int total = brown + yellow;
    int s = (brown + 4) / 2;
    
    for(int M = 3; M < s; M++){
        int N = s - M;
        if(N * M == total){
            answer.push_back(N);
            answer.push_back(M);
            return answer;
        }
    }
    
}