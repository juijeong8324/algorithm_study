// Link : https://programmers.co.kr/learn/courses/30/lessons/12950

#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<vector<int>> solution(vector<vector<int>> arr1, vector<vector<int>> arr2) {
    vector<vector<int>> answer; // 답이 되는 2차원 벡터
    vector<int> answer1; // 1차원 벡터 즉 행의 한 벡터를 담당할 친구들이다

    for(int i= 0; i < arr1.size(); i++){ // 행의 개수 담당
        for(int j=0; j < arr1[0].size(); j++){ // 열의 개수 담당
            answer1.push_back(arr1[i][j] + arr2[i][j]); 
            // 인덱스로 접근할 수 있는 건 원소가 있을 때만. 메모리에 할당이 안 되었으므로 push_back을 사용
            // 한 행에 대한 벡터 배열을 저장하고 
        }
        answer.push_back(answer1); // 한 행을 전체 벡터의 한 원소로서 저장! 
        answer1.clear(); //초기화 push_back은 마지막 원소 다음에 저장하기 때문에 초기화 시켜주장
    }
    return answer;
}
