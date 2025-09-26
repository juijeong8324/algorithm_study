#include <bits/stdc++.h>

using namespace std;

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int N, M; // 정수
	cin >> N >> M;

	int** arr = new int* [N]; // 행 받기 - 이때 크기가 n인 INT* 배열을 가리키는 포인터 변수 정의
	int** d = new int* [N]; // 거리 받기 
	for (int i = 0; i < N; i++) {
		arr[i] = new int[M]; //열받기
		d[i] = new int[M]; // 거리 열 받기 
	}

	for (int i = 0; i < N; i++) {
		string temp; // 임시저장
		cin >> temp;
		for (int j = 0; j < M; j++) {
			arr[i][j] = temp[j] - '0'; // 값 넣기, 그냥 int(temp[j])로 두면 49가 나온다. 
			d[i][j] = 0; // 초기화 
		}
	}

	queue<pair<int, int>> q; // 큐를 만들어줌 
	q.push({ 0,0 }); // 초기 위치 값 넣기 
	int dx[4] = { 1,0,-1,0 }; // 시계방향으로
	int dy[4] = { 0,1,0,-1 };
	while (!q.empty()) {
		pair<int, int> temp = q.front(); //앞의 값 꺼내기 
		q.pop();
		for (int i = 0; i < 4; i++) {
			int x = temp.first + dx[i];
			int y = temp.second + dy[i];

			if (x < 0 || x >= N || y < 0 || y >= M) continue; // 미로 범위 밖일 경우
			if (d[x][y] > 0 || arr[x][y] != 1) continue; // 이미 접근했거나 0인 경우 

			// 접근 가능 
			d[x][y] = d[temp.first][temp.second] + 1; // 인접한 블록이므로!
			q.push({ x,y });

		}
	}

	cout << d[N - 1][M - 1] + 1; // 알고리즘에 따라...  

	// 해제 
	for (int i = 0; i < N; i++) {
		delete[] arr[i];
	}
	delete[] arr;

}
