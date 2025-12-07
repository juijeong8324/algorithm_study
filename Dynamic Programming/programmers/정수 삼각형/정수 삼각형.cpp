// Input
// triangle = 삼각형 정보가 담긴 배열 (삼각형 높이 1 ~ 500) (삼각형 숫자 0 ~ 9999)
// Output
// 삼각형 꼭대기에서 바닥까지 이어지는 경로 중 거쳐간 숫자의 최댓값
// 아래칸 이동 시 대각선 방향으로 한 칸 오른쪽 또는 왼쪽
// Hint
// Brtue Force + DFS? = 문제는 높이가 500…. 이는 방문할 수 있는 모든 경로의 경우의 수는 2^{500} 가지…
// 결국 모든 경로를 확인해야 하는데, 한 경로만을 끝까지 파서 확인하고 뒤로가는 방법은 이미 앞에서 계산한 값을 또 계산해야 하므로 비효율적!
// DP = 꼭대기에서 바닥까지 이어지는 경로 중 거쳐간 숫자의 최대 합 → k번째 레벨에서 현재 노드까지의 최대합으로 분할
// dp[k][i] = k레벨의 i번째 노드의 최댓값!

#include <bits/stdc++.h>

using namespace std;

int solution(vector<vector<int>> triangle) {
    int answer = 0;
    int h = triangle.size(); // 삼각형의 높이 
    vector<vector<int>> dp(h, vector<int>(h, 0)); // 2차원 배열 생성 
    
    dp[0][0] = triangle[0][0]; // 초기화 
    
    for(int k=0; k < h-1; k++){ // 현재 k층을 기준으로 다음 노드 레벨(k+1) 선택 
        for(int i= 0; i < k+1; i++){ // k층에는 원소가 k+1개 존재 (0-index이므로) 
            // 1. 현재 노드 기준으로 왼쪽 아래 
            dp[k+1][i] = max(dp[k+1][i], dp[k][i]+triangle[k+1][i]); 
            // 2. 현재 노드 기준으로 오른족 아래 
            dp[k+1][i+1] = max(dp[k+1][i+1], dp[k][i]+triangle[k+1][i+1]); // 기존값, 현재 노드 기분 오른쪽 아래 
        }
    }

    for(int i = 0; i < h; i++){
        answer = max(dp[h-1][i], answer);
    }
    return answer;
}