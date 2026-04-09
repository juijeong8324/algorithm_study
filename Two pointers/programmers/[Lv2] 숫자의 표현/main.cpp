#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 1; // 자기자신
    int start = 1; 
    int end = start;
    int temp_sum = start;
    
    if(n == 1){
        return answer;
    }
    
    while(start != n && end != n){
        if(temp_sum < n){
            end++;
            temp_sum += end;
        }
        else if(temp_sum > n){
            temp_sum -= start;
            start++;
        }
        else{
            answer++;
            temp_sum -= start;
            start++;
        }
    }
    
    return answer;
}