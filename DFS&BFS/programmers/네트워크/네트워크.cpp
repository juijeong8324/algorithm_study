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
    DFS / BFS = 깊이든 너비든 연결된 노드를 모두 탐색 
    한번 방문했으면 탐색 취소 
*/

#include <string>
#include <vector>
#include <stack>

using namespace std;

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    vector<bool> vis(n, 0); // n개를 모두 0으로 초기화 
    stack<int> s;
    
    for(int i = 0; i < n; i++){
        if (vis[i] == 1) // 시작점이 이미 방문했다면
            continue;
        
        answer += 1;  // 네트워크 추가 
        s.push(i);
        vis[i] = 1;
            
        while(!s.empty()){
            int curr = s.top();
            s.pop(); // 제거 
            
            for(int j=0; j < n; j++){
                if (computers[curr][j] == 1 && vis[j] != 1){
                    s.push(j);
                    vis[j] = 1;
                }
            }
        }
    }
    
    return answer;
}