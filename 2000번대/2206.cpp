#include <bits/stdc++.h>

using namespace std;

// ���� ������ �ξ�� �޸� �ʰ� ��� �ȶ��. 
const int SIZE = 1000; // �迭 �ִ� ũ��
string arr[SIZE]; // �� 
int d[SIZE][SIZE][2]; // �Ÿ��� ���� �� 

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int N, M; // ����
	cin >> N >> M;

	for (int i = 0; i < N; i++) {
		cin >> arr[i]; // �� ���� �޾ƿ��� 
	}

	queue<pair<pair<int, int>, int>> q; // BFS ������ ���� ť 
	q.push({ {0,0},1 }); // ������ �ֱ�, �� �μ� �� ���� 
	d[0][0][1] = 1; // �̹� �湮 
	int dx[4] = { 0,1,0,-1 };
	int dy[4] = { 1,0,-1,0 };

	while (!q.empty()) {
		int x = q.front().first.first;
		int y = q.front().first.second;
		int breaked = q.front().second;
		q.pop(); // �� �� ������ �������� 

		if (x == N - 1 && y == M - 1) {
			cout << d[x][y][breaked]; // �������̸� 
			return 0; // ���� 
		}

		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue; // �̷� �� ������ ��� 
			if (arr[nx][ny] == '1' && breaked) // ���ε� �μ� �� �ִ� ��� 
			{
				q.push({ {nx,ny},0 }); // ť�� �߰� 
				d[nx][ny][0] = d[x][y][1] + 1; // �Ÿ� ������Ʈ 

			}
			else if (arr[nx][ny] == '0' && !d[nx][ny][breaked]) {
				// �湮�� �� �ִ� ����̰� �湮�� ���� ���� ����� ��� 
				q.push({ {nx,ny}, breaked });
				d[nx][ny][breaked] = d[x][y][breaked] + 1; // �Ÿ� ������Ʈ 
			}

		}
	}

	cout << "-1"; // ���������� ���� 
	return 0;

}
