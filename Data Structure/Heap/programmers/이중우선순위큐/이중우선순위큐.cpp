// # Input
// # operations = 이중 우선순위 큐가 할 연산 
// #            = 길이가 (1, 1,000,000) 인 문자열 배열 
// # Output
// # 모든 연산 처리 후 큐가 비어있으면 [0,0] 않으면 [최댓값, 최솟값]
// # 명령어
// # I 숫자 = 큐에 주어진 숫자 삽입
// # D 1 = 큐에서 최댓값 삭제 
// # D -1 = 큐에서 최솟값 삭제 
// Hint
// 최대힙과 최소힙을 이용해서 동기화 
// priority_queue는 최대힙으로 구현 

#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <unordered_map>

using namespace std;

vector<int> solution(vector<string> operations) {
    priority_queue<int> max_heap;
    priority_queue<int, vector<int>, greater<int>> min_heap;
    unordered_map<int,int> count;
    
    for (auto op : operations){
        char c = op[0];
        int num = stoi(op.substr(2));
        
        if(c == 'D'){
            if(count.empty()) continue;
            
            if(num == 1){ // 최댓값 삭제 
                // max_heap 동기화 
                while(!max_heap.empty() && count[max_heap.top()] == 0){ // 기존에 삭제된 원소라면 
                    max_heap.pop();
                }
                if(!max_heap.empty()){ // 제거할 수 있는 원소가 남아있다면 
                    count[max_heap.top()]--;
                    max_heap.pop();
                }
            }
            else{ // 최솟값 삭제 
                // max_heap 동기화 
                while(!min_heap.empty() && count[min_heap.top()] == 0){ // 기존에 삭제된 원소라면 
                    min_heap.pop();  
                }
                if(!min_heap.empty()){ // 제거할 수 있는 원소가 남아있다면 
                    count[min_heap.top()]--;
                    min_heap.pop();
                }
            }
            
        }
        else{ 
            max_heap.push(num);
            min_heap.push(num);
            count[num]++;
        }
    }
    
    while(!max_heap.empty() && count[max_heap.top()] == 0){
        // 기존에 삭제된 원소라면 
        max_heap.pop();
    }
    while(!min_heap.empty() && count[min_heap.top()] == 0){
        // 기존에 삭제된 원소라면 
         min_heap.pop();
    }
    
    if(max_heap.empty() && min_heap.empty()){
        return {0,0};
    }
    else{
        return {max_heap.top(), min_heap.top()};
    }
    
}