/* 
Input
    n = 컴퓨터 개수 (1 이상 200 이하) 
    computers = 연결에 대한 정보가 담긴 2차원 배열 (0부터 n-1인 정수)
        i번 - j번 컴퓨터 연결: computers[i][j] = 1, 즉 양방향임을 알 수 있음
Output
    네트워크의 개수 
    네트워크란 
    A - B → B - C → C - A임! = A,B,C는 모두 같은 네트워크! 
Hint
    Union Find
    같은 네트워크면 같은 노드 번호 
*/

#include <string>
#include <vector>
#include <set>

using namespace std;

int solution(int n, vector<vector<int>> computers) {
    vector<int> node(n, 0); // n개를 모두 0으로 초기화 
    
    for(int i=0; i < n; i++){
        node[i] = i;
    }
    
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            if(computers[i][j] == 1){ 
                // Union network i to network j
                for(int k = 0; k<n; k++){
                    if(node[k] == node[i]){ // k in network i
                        node[k] = node[j];
                    } 
                }
            }
        }
    }
    
    set<int> answer;
    // node를 set으로 
    for(int i=0; i < n; i++){
        answer.insert(node[i]);
    }
    return answer.size();
}