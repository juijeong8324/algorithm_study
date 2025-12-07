#include <bits/stdc++.h>

using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    priority_queue<int, vector<int>, greater<int>> q;
    
    for(int i=0; i < scoville.size(); i++){
        q.push(scoville[i]);
    }
    
    while(true){
        if(q.top() >= K){
            break;
        }
        
        if(q.size() == 1){
            return -1;
        }
        
        if(q.top() >= K){
            break;
        }
        
        else{
            int first = q.top(); q.pop();
            int sec = q.top(); q.pop();
            q.push(first + (sec*2));
            answer++;
        }
    }
    
    return answer;
}